from InputSystem.States.States import Fetch, Check


class InputSystem:

  def __init__(self):
    self.machine = InputSystemStateMachine()

  def set_valid_commands(self):
    pass

  def run(self):
    self.machine.run()

  def early_initialization(self, earlyinitdict):
    self.machine.early_initialization()
    for key in earlyinitdict.keys():
      if key == "Commands":
        self.machine.set_commands(earlyinitdict[key])


class InputSystemStateMachine:

  def __init__(self):
    self._currentState = None
    self._user_data = None
    self.validInput = None
    self.validcommandsformat = None
    self.statesDict = {"Fetch": Fetch(), "Check": Check()}

  def early_initialization(self):
    self.validInput = dict()
    self.validcommandsformat = dict()

  def set_commands(self, commands):
    for key, value in commands.items():
      self.validInput[key] = value

  def set_command_format(self, format):
    for key, value in format.items():
      self.validcommandsformat[key] = value

  def transition_to(self, statename):
    self._currentState = self.statesDict[statename]
    self._currentState.context = self
    self._currentState.run()

  def run(self):
    self.transition_to("Fetch")

  def set_data(self, data):
    self._user_data = data

  def get_data(self):
    return self._user_data
