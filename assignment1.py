"""
#We are evaluating a binary classification model. We have the number of true positives, true
negatives, false positives, and false negatives for confidence score thresholds 0.1, 0.2, 0.3, ...,
0.9 respectively (feel free to assume the data structure for this input data and provide an
explanation).
Write a function to return THE BEST threshold that yields a recall >= 0.9. Unit tests for
this function are also encouraged.
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_score = 2 * (precision * recall) / (precision + recall)
assume that
threshold_res= {0.1 :(TP1, FP1, TN1, FN1), 0.2 :(TP2, FP2, TN2, FN2), 0.3 :(TP3, FP3, TN3, FN3),
0.4: (TP4, FP4, TN4, FN4),  0.5 :(TP5, FP5, TN5, FN5),  0.6 :(TP6, FP6, TN6, FN6), 0.7 :(TP7, FP7, TN7, FN7),
0.8 :(TP8, FP8, TN8, FN8),  0.9 :(TP9, FP9, TN9, FN9)},
 to choose the "best" threshold, is to prefer the threshold that yields highest F1 score and high accuracy
 once the recall condition is met.

"""

from typing import List, Tuple, Dict


def find_best_threshold(
    threshold_res: Dict[float, Tuple[int, int, int, int]], exp_recall: float
) -> float:
    """
      Finds the best threshold that yields a recall >= exp_recall
      :param threshold_res: Dictionary with threshold as key and value is corresponding tuple of (TP, FP, FN, TN)
      :param exp_recall: expected recall value
      :return: float: The best threshold that satisfies recall >= 0.9, with the highest F1 score.
             If multiple thresholds have the same F1 score, the one with the highest accuracy is returned.
    .
    """
    best_threshold = None
    best_f1_score = 0
    best_accuracy = 0

    for threshold in threshold_res:
        value = threshold_res.get(threshold)

        recall = (
            (value[0] / (value[0] + value[3])) if value[0] + value[3] != 0 else 0
        )  # TP/(TP+FN)
        precision = (
            value[0] / (value[0] + value[1]) if (value[0] + value[1]) != 0 else 0
        )  # TP / (TP + FP)
        accuracy = (
            (value[0] + value[2]) / (value[0] + value[1] + value[2] + value[3])
            if (value[0] + value[1] + value[2] + value[3]) != 0
            else 0
        )
        f1_score = (
            2 * (precision * recall) / (precision + recall)
            if (precision + recall) != 0
            else 0
        )

        if recall >= exp_recall:
            if (f1_score > best_f1_score) or (
                (f1_score == best_f1_score) and (accuracy > best_accuracy)
            ):
                best_f1_score = f1_score
                best_accuracy = accuracy
                best_threshold = threshold

    return best_threshold
