# Consider a string of ones and zeros representing an unsigned binary integer. Design and
# implement a solution that will compute the remainder when the represented value is divided by
# three.

import logging


class FiniteAutomation:
    """
    A class of a Finite Automaton (FA),  FA is a model used to simulate a system with a
    finite number of states. The FA accepts strings of symbols and can change states based on input symbols.

    Attributes:
        set_of_states (tuple): The set of all possible states in the automaton.
        input_alphabet (tuple): The set of all possible input symbols that the automaton can process.
        initial_state (string): The initial state of the automaton from where it starts processing.
        set_of_final_states (tuple): The set of acceptable final states where the automaton can end up after processing inputs.
        transition (dict): A dictionary representing the transition function, mapping a (state, input) pair to a new state.
        _current_state (string): The current state of the automaton during processing.
    """

    def __init__(
        self, set_of_states, input_alphabet, set_of_final_states, initial_state
    ):
        """
        Initializes the FiniteAutomation with the provided set of states, input alphabet, final states, and initial state.

        Args:
            set_of_states (tuple): The set of all possible states in the automaton.
            input_alphabet (tuple): The set of all possible input symbols that the automaton can process.
            initial_state (string): The initial state of the automaton from where it starts processing.
            set_of_final_states (tuple): The set of acceptable final states where the automaton can end up after processing inputs.
        """
        self.set_of_states = set_of_states
        self.input_alphabet = input_alphabet
        self.initial_state = initial_state
        self.set_of_final_states = set_of_final_states
        self.transition = {}
        self._current_state = initial_state

    def add_transaction(self, input_state, input_alphabet, output_state):
        """
        Adds a transition rule to the automaton's transition function.

        Args:
            input_state (str): The state from which the transition occurs.
            input_alphabet (str): The input symbol that triggers the transition.
            output_state (str): The state after the transitions.

        Raises:
            ValueError: If the input state, output state, or input alphabet are not in the valid range.
        """
        if (
            (input_state in self.set_of_states)
            and (output_state in self.set_of_final_states)
            and (input_alphabet in self.input_alphabet)
        ):
            self.transition[(input_state, input_alphabet)] = output_state
        else:
            logging.error(
                f"invalid input,{input_alphabet} should belong to {self.input_alphabet}, {input_state} "
                f"should belong to {self.set_of_states}, {output_state} should belong to {self.set_of_final_states} "
            )

    @property
    def current_state(self):
        """
        Gets the current state of the automaton.
        Returns:
            string: The current state.
        """
        return self._current_state

    @current_state.setter
    def current_state(self, input_alphabet):
        """
        Set the current state of the automaton based on the input alphabet.

        Args:
            input_alphabet (string): The input symbol that triggers the transition.

        Raises:
            ValueError: If the input alphabet is not in the defined input alphabet set.
        """
        if input_alphabet in self.input_alphabet:
            self._current_state = self.transition[(self.current_state, input_alphabet)]
        else:
            logging.error("wrong alphabet")
            raise ValueError

    def current_state_transition(self, input_string):
        """
        Processes an input string and updates the automaton's current state accordingly.
        Args:
            input_string (str): A string of input symbols to be processed by the automaton.
        Raises:
            ValueError: If any symbol in the input string is not in the input alphabet set.
        """
        for i in input_string:
            self.current_state = i
