---
title: "Messy Digital Workspace"
date: 2022-05-28T00:00:00-04:00
draft: true
tags: [work]
---

While learning about 12 new tools simultaneously without much guidance, my
computer quickly became overrun with notes, files, snippets, and links in
various file formats in every nook and cranny of my filesystem. One of my worst
offenses was taking notes in Sublime or VS Code by opening a new file (in
whatever project workspace happened to be open) and then leaving it open in the
editor, sentencing the new information to memory limbo instead of committing to
a directory where it truly belonged.

Now, in my fantasy utopia, every bit of data would belong explicitly to one
obvious parent category or topic. But alas, we live in a very real world. Do my
draw.io UML diagrams and screenshots of SQL schemas taken during a screenshare
call belong in `Pictures`, in `Documents` next to all the
code-challenge-related PDFs sent via email, or in `Code` alongside the actual
GitHub repository clones?

I've never trusted OS-level search functionality, except for quickly opening
apps on Mac with Spotlight, or opening the right Settings page in Windows
(since the alternative would be clicking through at least 3 ambiguous links and
child pages under "Settings," at least on Windows 7).

The best solution I have found for quickly finding and managing files and
generic data on my computer is based on 2 key traits:

1. Use plaintext wherever possible

https://plaintext-productivity.net/

2. Make a local data lake (or data pond) by throwing everything related into
one folder and opening that as a workspace in VS Code

- Regex search all files
- Fuzzy-match filename with ctrl+P

## TODO

I still need to come up with a way of an efficient and low-friction work log.
I'm thinking of a shell script or app to open a window with just a textarea, a
pre-populated `Create date` field, and a `Log` button to save my plaintext
somewhere.

I'd use it all the time for one-liner diary entries like "SonarQube integration
might be an issue" or "Priority is now Loki integration." Then a quick `grep`
or workspace search would allow me to refresh my memory of what issues arose
when and how priorities changed over time.
