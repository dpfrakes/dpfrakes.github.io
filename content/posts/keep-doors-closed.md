---
title: "Keep Some Doors Closed"
date: 2022-10-14T00:00:00-04:00
draft: true
tags: [work]
---

In my junior year of high school, I was accidentally enrolled in AP Computer
Science. I like to think this was due to the most ironic software bug of my
life somewhere in the school's course enrollment system.

Our first assignment was to write a "Hello World" Java program. Java and C++
are often the programming languages of choice for teachers as they are
compiled, strongly typed, and ~old~ mature languages. That also means they can
be quite verbose.

```java
public class HelloWorldProgram {

    public static void main(String[] args) {
        System.out.println("Hello world!");
    }

}
```

We received the assignment as a printout that included setup instructions and
the above source code. Our job was to type out the code ourselves, compile it,
and run it.

Being the inquisitive mind that I am, I felt this was cheating. I "made" a
program that did what I wanted it to, but the only thing I understood was that
I could change `"Hello world!"` to something else and the program would display
the new message instead. The rest of it? No idea.

What's `public`? What's `static`? `void`? `class`? `String`? What's with the
square brackets? How come there's a `public` chunk of code inside another
chunk of `public` code? Is that necessary? Why do I need to specify `System`?
What else is `System` capable of other than `out.println`?

This was too many questions for the teacher. (Admittedly, he was not a good
teacher.) He got annoyed with the barrage of questions I started to spew,
saying we'd get to it. I was impatient, annoyed that this teacher was not
willing to encourage my inquisitive nature and quench my thirst for knowledge.

Of course, it wasn't until long after high school that I realized the point of
not sharing these answers: It would take roughly half a semester to learn the
answers, which is exactly why we did get to these answers later. Sure, I could
have been given brief answers without explanation and a link to some Java
documentation, but I wouldn't learn anything.

Opening all those doors would mean getting confused, lost, intimidated, and
discouraged. If the teacher had answered all my questions on day one, he
would've essentially assigned me about 40 pages of boring documentation to
read (not including any subtopics, exercises, or assessments):

- [Access Control](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html) (849 words)
- [System](https://docs.oracle.com/javase/7/docs/api/java/lang/System.html) (4,457 words)
- [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) (10,583 words)
- [Class](https://docs.oracle.com/javase/tutorial/java/concepts/class.html) (514 words)
- [Class Methods](https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html) (1,186 words)
- [Arrays](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html) (1,713 words)

Learning happens one step at a time ([Scaffolding](https://en.wikipedia.org/wiki/Instructional_scaffolding)).

It's like being in a labyrinth versus a hallway: if there are just endless
options to navigate, you'll almost assuredly go wrong many times. _"I have no
idea where to go next."_ Instead, wouldn't you rather have all doors closed
and locked except one? _"Well I know where I'm going now."_ It will still take
you a long time, as any true learning requires, but the fewer bad options are
before you, the less likely you'll make one.

This is why curriculum development isn't just a list of topics to learn: it's
an architected roadmap to take a complicated, multi-faceted web of obstacles
and design a linear path to explore it all.

[!https://camo.githubusercontent.com/b6482a1fcf61b0f1b479c9f129b00e09ffb100026db15502b351b083f4f5fd3f/687474703a2f2f6e6972766163616e612e636f6d2f74686f75676874732f77702d636f6e74656e742f75706c6f6164732f323031332f30372f526f6164546f44617461536369656e74697374312e706e67]

TL;DR

Figure out the next best door to open. If you don't know, ask someone who's
already been in the room you're in now (or close to it). Then, open that door
and ONLY that door. Learn, rinse, repeat.
