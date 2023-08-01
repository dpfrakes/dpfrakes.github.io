---
title: "CLI Diary"
date: 2022-05-28T00:00:00-04:00
draft: false
tags: [work]
---

In my endless pursuit of a minimal-barrier-to-entry method of tracking notes
and tasks, I have tried various apps, including Google Docs, OneNote, Evernote,
Notion, Obsidian, and just plain old Markdown. Each has its pros and cons, but
for my everyday "I should write that down" moments, I recently thought of a new
method I think I'm going to try.

[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Don't Repeat
Yourself) is a popular software development principle that advocates the
avoidance and removal of redundancy in code. I try to apply that principle to
my work at large: If I'm going to have to do a task repeatedly, it may be worth
investing time in a tool or method to ease the burden of doing said task each
iteration.

More relevantly, however, DRY can also be applied in a different manner. If a
system is already in use that can be leveraged to solve a new problem, use it
instead of introducing a new system that may require maintenance and debugging
in the future. In other words:

![forest-gump.gif](../_resources/forest-gump.gif)

Since I'm in love with my terminal (what self-respecting software engineer
isn't?), I figured I'd make use of the rich environment in which I'm already
operating, teeming with mature, time-tested tools.

Since everything you run in your terminal is logged (see
`tail ~/.zsh_history`), you could run anything you wanted as a shell comment
to avoid running anything while still logging your input to a file:

```sh
$ # I should learn Go... tutorial here https://go.dev/doc/tutorial/getting-started
$ history -E

```

The only next step would be to create an ETL pipeline to extract, transform,
and load those messages to a separate storage format, like a Postgres database,
or to a messaging queue, like Kafka.

## Business Idea

Build a collection of data transformers to convert each note-taking app to a
standardized format. Then build a collection of data transformers that load
a standardized note or task to each source. Markdown is probably best for the
standardized format, no?

```
                 ┌─────────┐
 Google -------> │         │ -------> Google
  Docs           │         │           Docs
                 │         │
 OneNote ------> │         │ ------> OneNote
                 │  *.md   │
EverNote ------> │    /    │ ------> Evernote
                 │ *.html  │
 Notion -------> │         │ -------> Notion
                 │         │
Obsidian ------> │         │ ------> Obsidian
                 └─────────┘
```
