
import InputSystem.System as SY
if __name__ == "__main__":
    earlyinitdict = {"Commands":{},"ValidCommandsFormat":{}}
    system = SY.InputSystem()
    system.early_initialization(earlyinitdict)
    system.run()
