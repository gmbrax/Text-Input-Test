
class State:
    def __init__(self):
        self.context = None

    def run(self):
        pass
        # Method to be overridden as the  entrypoint of subclass


class Fetch(State):
    def __init__(self):
        super().__init__()

    def run(self):
        user_input = input("Command -> ")
        self.context.set_data(user_input)
        self.context.transition_to("Check")


class Check(State):
    def __init__(self):
        super().__init__()

    def run(self):
        data = self.context.get_data()
        print(data)
        self.context.transition_to("Fetch")


class Validate(State):
    def __init__(self):
        super().__init__()

    def run(self):
        data = self.context.get_data()
        print(data)


class Execute(State):
    def __init__(self):
        super().__init__()

    def run(self):
        data = self.context.get_data()
        print(data)

