---
title: "Digital Forensics"
date: 2021-09-29T00:00:00-04:00
draft: false
tags: [tech]
---

Exploring the magic black box of `.git`

## What happened and when?

When something breaks, and you have no idea where to start, try a manual binary search through the git log.

1. something is currently broken
2. we don't know when it broke / when it last worked

What to do

1. `git log --pretty=format:"%ci | %h" --no-merges -- tools/ui-ide/package.json`
2. Start at middle commit ID
3. check out commit ID and run whatever idempotent script you need to
4. put comment next to commit ID
5. If it works, pick commit ID halfway between that one and last-tried future commit (or latest commit)
6. If it doesn't work, pick commit ID halfway between that one and last-tried past commit (or first commit)
7. Repeat from step 3 with new commit ID

Once this is done, you'll have determined which commit ID broke everything and you can blame the developer who created that commit
