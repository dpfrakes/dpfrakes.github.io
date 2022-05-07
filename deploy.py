from bs4 import BeautifulSoup
from halo import Halo
import os
import subprocess
import traceback


def progress(args, loading="Loading...", success="Succeeded"):
    spinner = Halo(loading)
    spinner.start()
    try:
        completed = subprocess.run(args.split())
        if completed.returncode == 0:
            spinner.succeed(success)
        else:
            spinner.fail(completed.stderr)
    except Exception as e:
        spinner.fail()
        traceback.print_exception(type(e), e, e.__traceback__)


# Gather metadata to check when last updates to jupyter notebooks were
# TODO subprocess.run(["git"])

# Convert jupyter notebooks into posts
progress(
    "/home/dpfrakes/.virtualenv/ds/bin/jupyter nbconvert --to html --template basic notebooks/*.ipynb",
    "Converting jupyter notebooks...",
    "Jupyter notebooks converted"
)

# Parse exported jupyter notebooks to be repurpose as blog posts
notebooks = subprocess.run(["find", "notebooks", "-name", "*.html"], capture_output=True).stdout.decode().split("\n")[:-1]
notebook_html = {}

for notebook in notebooks:

    # Use filename (without extension) as post slug
    slug = notebook[len("notebooks/"):].replace(".html", "")

    # Save notebook as post
    notebook_post = os.path.join("content", "posts", f"{slug}.md")

    # Create new post if it doesn't already exist using hugo
    if not os.path.exists(notebook_post):
        subprocess.run(["hugo", "new", os.path.join("posts", f"{slug}.md")])
    
    # Converted jupyter notebooks converted using `basic` template are
    html = None
    title = slug.title().replace("-", " ")
    with open(notebook) as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        html = soup.decode_contents()

        # If content start with an h1, use it as post title, otherwise use slug
        notebook_h1 = soup.select("div.text_cell:first-child > div.inner_cell > div.text_cell_render:first-child > h1:first-child")
        if notebook_h1:
            title = notebook_h1[0].text[:-1]
            html = html.replace(notebook_h1[0].decode_contents(), "")
        
        # Save notebook HTML for injection later
        # notebook_html[slug] = html

    # Overwrite notebook content if applicable
    with open(notebook_post, "a") as f:
        f.write(html)
    
    # Replace title in post front matter meta if applicable

    # Remove converted notebook from `notebooks` dir
    subprocess.run(["rm", notebook])

# Build hugo site
progress(
    "hugo -D",
    "Building hugo site...",
    "Hugo site built"
)

# # Replace JUPYTER_NOTEBOOK_CONTENT with HTML in `public` dir
# for slug, html in notebook_html.items():
#     content = None
#     public_notebook = os.path.join("public", "posts", slug, "index.html")
#     with open(public_notebook, "r") as f:
#         content = f.read()
#         content = content.replace("<p>JUPYTER_NOTEBOOK_CONTENT</p>", html)
#     if content is not None:
#         with open(public_notebook, "w") as f:
#             f.write(content)
