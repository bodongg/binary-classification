# Read the held-out results

The [published confusion matrix](../README.md#confusion-matrix) has 81 true negatives, 19 false positives, 7 false negatives, and 18 true positives.

| Measure | Calculation | Result |
| --- | --- | ---: |
| Accuracy | (81 + 18) / 125 | 0.792 |
| Buyer precision | 18 / (18 + 19) | 0.486 |
| Buyer recall | 18 / (18 + 7) | 0.720 |
| False-positive rate | 19 / (81 + 19) | 0.190 |

The model flags 37 customers to reach 18 buyers. An always-negative baseline flags nobody and misses all 25 buyers, even though its accuracy is slightly higher.

If the decision threshold changes, choose it using validation data or cross-validation within the training split. Compare the number of buyers reached and the number of non-buyers flagged against the intended outreach budget. Evaluate the final choice once on the reserved test set.
