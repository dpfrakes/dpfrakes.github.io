---
title: "Evaluating ML Models"
date: 2022-10-15T00:00:00-04:00
draft: false
tags: [tutorials]
---

## F1 Score

F-score is the measure of a test's accuracy.

F1 is a great metric for all classification models, but particularly those
built using imbalanced datasets (e.g. a lot more positive cases than negative)
because it takes precision and recall into consideration:

$$F1 = 2 * \frac{precision * recall}{precision + recall}$$

The F1 score evaluates to a value between 0 and 1, 0 being "all observations
were incorrect" and 1 being a perfect score. A middle score around 0.5
indicates that precision is high but recall is low, or vice versa.




