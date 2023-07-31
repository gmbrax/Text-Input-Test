from InputSystem.States.States import Fetch, Check


class InputSystem:
    def __init__(self):
        self.machine = InputSystemStateMachine()

    def set_valid_commands(self):
        pass


class InputSystemStateMachine:
    def __init__(self):
        self._currentState = None
        self._data = None
        self.statesDict = {"Fetch": Fetch(), "Check": Check()}
        self.transition_to("Fetch")

    def transition_to(self, statename):
        self._currentState = self.statesDict[statename]
        self._currentState.context = self
        self._currentState.run()

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data
