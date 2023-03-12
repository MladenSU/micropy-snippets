class LightControl:
    def __init__(self, errorPin: int, successPin: int, inProgressPin: int):
        self.errorPin = Pin(errorPin, Pin.OUT)
        self.successPin = Pin("LED", Pin.OUT) if not successPin else Pin(successPin, Pin.OUT)
        self.inProgressPin = Pin(inProgressPin, Pin.OUT)
        pass

    @staticmethod
    def _blinker(blinkPin, blinkFreq: int, blinkReps: int) -> None:
        """Turn ON and OFF a pin for specific number of times with specific frequency"""
        while blinkReps > 0:
            blinkPin.toggle()
            sleep(blinkFreq)
            blinkReps -= 1
        blinkPin.value(0)

    def _lightCleanUp(self):
        print("Clean-up triggered)")
        self.errorPin.value(0)
        self.successPin.value(0)
        self.inProgressPin.value(0)

    def lightNotification(self, outputStatus: int, blinkFreq: float = 0.5, blinkReps: int = 5) -> None:
        """Based on the outputStatus (0-2) a pin will be triggered\n
        0 - should be used for success\n
        1 - should be used for fail\n
        2 - should be used for thinking\n"""
        if outputStatus == 0:  # in cases status is 1 - fail
            self.inProgressPin.value(0)
            print("Toggling Success")
            self._blinker(self.successPin, blinkFreq, blinkReps)
        elif outputStatus == 1:
            print("Toggling Error")
            self.inProgressPin.value(0)
            self._blinker(self.errorPin, blinkFreq, blinkReps)
        else:
            print("Toggle Thinking")
            self.inProgressPin.value(1)