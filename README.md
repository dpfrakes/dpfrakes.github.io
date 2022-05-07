# Personal website

See https://gohugo.io/hosting-and-deployment/hosting-on-github/

## TODO

1. Consolidate all posts to ~/dev/dpfrakes.github.io
2. Copy metadata to front matter (publish dates, tags, categories, etc)
3. Remove old repos/code
4. Run the following in the dpfrakes.github.io repo:

```sh
hugo -D
git push
```

## Publishing Workflow

Custom workflow via git hook (local) unless there's a way to install and run
`nbconvert` on remote server using GitHub Actions:

```sh
deploy
# hugo
# nbconvert --to html --template basic ./notebooks/*.ipynb
# cp ./
```

## Follow-up

1. Re-import site to Forestry
2. Customize theme to more minimal structure

## Static site

cd ~/dev/dpfrakes-site
cd ~/dev/sudo-better
cd ~/dev/NEWSITE/sudo-better
