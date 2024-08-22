import pytest
from assignment1 import *


@pytest.fixture
def threshold_res():
    threshold_dict = {
        0.1: (50, 5, 45, 10),
        0.2: (48, 4, 46, 12),
        0.3: (45, 3, 47, 15),
        0.4: (60, 12, 38, 5),
        0.5: (55, 10, 40, 8),
        0.6: (54, 8, 42, 6),
        0.7: (49, 6, 44, 11),
        0.8: (53, 7, 43, 7),
        0.9: (51, 5, 45, 9),
    }
    return threshold_dict


@pytest.mark.parametrize(
    "recall, expected_threshold",
    [(0.9, 0.6), (0.8, 0.6), (0.7, 0.6), (0.5, 0.6), (1, None)],
)
def test_find_best_threshold(threshold_res, recall, expected_threshold):

    best_threshold = find_best_threshold(threshold_res, recall)
    assert best_threshold == expected_threshold
