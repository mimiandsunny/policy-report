import pytest
from assignment2 import *


def test_add_transaction():
    fsm3 = FiniteAutomation(("s0", "s1", "s2"), ("0", "1"), ("s0", "s1", "s2"), "s0")
    fsm3.add_transaction("s1", "1", "s0")
    assert fsm3.transition == {("s1", "1"): "s0"}


@pytest.fixture
def fsm3a():
    fsm3 = FiniteAutomation(("s0", "s1", "s2"), ("0", "1"), ("s0", "s1", "s2"), "s0")
    fsm3.add_transaction("s0", "0", "s0")
    fsm3.add_transaction("s0", "1", "s1")
    fsm3.add_transaction("s1", "0", "s2")
    fsm3.add_transaction("s1", "1", "s0")
    fsm3.add_transaction("s2", "0", "s1")
    fsm3.add_transaction("s2", "1", "s2")
    return fsm3


def test_current_state(fsm3a):
    assert fsm3a.current_state == "s0"


@pytest.mark.parametrize(
    "test_string, expect_state",
    [
        ("101", "s2"),
        ("1010", "s1"),
        ("1101", "s1"),
        ("1100", "s0"),
        ("1110", "s2"),
        ("1", "s1"),
        ("", "s0"),
        ("101010", "s0"),
    ],
)
def test_current_state_set(fsm3a, test_string, expect_state):
    fsm3a.current_state_transition(test_string)
    assert fsm3a.current_state == expect_state


def test_invalid_alphabet(fsm3a):
    with pytest.raises(ValueError):
        fsm3a.current_state_transition("2")  # '2' is not in the input alphabet


def test_final_state_reachability(fsm3a):
    fsm3a.current_state_transition("100")
    assert fsm3a.current_state == "s1"


def test_no_transition_defined(fsm3a):
    fsm3a.transition.pop(("s0", "1"))
    with pytest.raises(KeyError):
        fsm3a.current_state_transition("1")
