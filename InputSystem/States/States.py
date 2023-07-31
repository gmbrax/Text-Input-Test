class State:

  def __init__(self):
    self.context = None

  def run(self):
    pass
    # Method to be overridden as the  entrypoint of subclass

  def transition_to(self, statename):
    self.context.transition_to(statename)


class Fetch(State):

  def __init__(self):
    super().__init__()

  def get_input(self):
    user_input = input("Command -> ")
    return user_input

  def set_context(self, data):
    self.context.set_data(data)

  def run(self):
    data = self.get_input()
    self.set_context(data)
    self.transition_to("Check")


class Check(State):

  def __init__(self):
    super().__init__()
    self.is_valid_input = None

  def get_data_from_context(self):
    return self.context.get_data()

  def run(self):
    data = self.get_data_from_context()
    print(data)


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
