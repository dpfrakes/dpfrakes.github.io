# README

This repository contains the source code and content for https://dpfrakes.dev.

## Site Development

```sh
# Run site locally
hugo server

# Run site with drafts
hugo server -D
```

## Site Deployment

Changes pushed to the `main` branch on the remote origin (GitHub) will
automatically trigger a build on the `gh-pages` branch. This is the branch
that is automatically deployed to `https://dpfrakes.github.io` (a feature of
GitHub). The content is then propagated to `https://dpfrakes.dev` via the DNS
settings (CNAME records) configured on the domain registrar (Google Domains).

## Notes

```sh
# Upgrade `hugo`
brew upgrade hugo
```

