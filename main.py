from abc import ABC


class InputSystem:
    _state = None

    def __init__(self):
        self.transition_to(Fetch())

    def transition_to(self, state):
        self._state = state
        self._state.inputsystem = self


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    def change(self, state):
        # fixMe: This can Lead to infinite recursion error
        self.context.transition_to(state)


class Fetch(State):
    def __init__(self):
        print("ping")
        self.change(Validade())


class Validade(State):
    def __init__(self):
        print("Pong")
        self.change(Fetch())


if __name__ == "__main__":
    print("Hellord")
    System = InputSystem()
