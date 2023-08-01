---
title: "Bi-Directional Data Architecture"
date: 2022-02-02T00:00:00-04:00
draft: false
tags: [tech]
---

I constantly think of software, data, and other technical components of my job
in terms of analogies. It's a great teaching mechanism, particularly for visual
learners such as myself.

Analogies have greatly impacted terminology in software for a long time. Data
pipelines are so named as information "flows" from a source to a destination.
Neural networks, and their building blocks called perceptrons, are named after
neurological terminology since the design of these structures was inspired by
the brain.

Reflecting on the newest (to me) buzzword - "data mesh" - made me think about
how else common software architectures can be thought of and how they might
improve in the next iteration of technical business needs.

As mentioned earlier, the idea of "pipelines" has been around for a while as a
descriptor for information flow. Maybe it's due to the fact that I live in the
DC area, but my brain immediately thought of traffic as a parallel analogy to
pipelines. Other than the content that flows inside pipelines (water) and
highways (vehicles), one might argue the biggest difference between them is the
fact that water tends to flow only in one direction: used water from the sink
doesn't travel back up the same pipe from whence it came.

Roads and highways, however, are typically bi-directional: we treat I-95 as one
road, but the use of the road could mean one outcome (southbound) or the exact
opposite (northbound).

This caused me to pause and wonder how this could be applied to software
architecture.

The most exciting part of this thought experiment was the natural progression
toward questioning a common assumption: data flows in one direction. After all,
if we have bad raw data stored in the source database, surely our analysis will
be negatively affected, and there is nothing to be done until the upstream data
is fixed.

This implies a bit of blame game: it's not the analyses' fault, it's the data.
What if you could fix the data from downstream? The decision-making
responsibility of how to edit the data remains with humans, but could be shared
between engineers and analysts.

The first step would be to add traceability to the entire data wrangling and
analysis workflow. This would leave a "trail of breadcrumbs" to lead back to
the source data at fault.

I'm thinking this would be a middleware of sorts, adding a private stack trace
to a generic data type, like pandas' `DataFrame`. Then each method that has the
potential of changing or aggregating the data would be added to this stack
trace when invoked.

## Problems

**Problem**

Analysts may edit data incorrectly, causing issues in other downstream
applications

**Solutions**

* Implement an "approval process" where analysts' changes must be reviewed and
approved by the data engineers responsible for data management

* Store the data edits in a separate architectural layer and have analysts
apply edits (patches) as they see fit
