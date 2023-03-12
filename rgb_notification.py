from picozero import RGBLED


class LightControl:
    def __init__(self, redPin: int, greenPin: int, bluePin: int):
        self.rgbLight = RGBLED(red=redPin, green=greenPin, blue=bluePin)

    def _lightCleanUp(self):
        """Used in case RBG is not turned off"""
        print("Clean-up triggered)")
        self.rgbLight = (0, 0, 0)

    def _blink(self, color: str, blinkFreq: float, blinkReps: int) -> None:
        """A short function for lightNotification().
        Available colors:
            - red
            - green
            - blue
            - off (shut down)"""
        colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "off": (0, 0, 0)}
        self.rgbLight.blink(on_times=(1, blinkFreq), colors=(colors[color], (0, 0, 0)), wait=True, n=blinkReps)

    def lightNotification(self, outputStatus: int = 2, blinkFreq: float = 0.5, blinkReps: int = 2) -> None:
        """Based on the outputStatus (0-2) a color will be triggered\n
        0 - should be used for success\n
        1 - should be used for fail\n
        2 - should be used for thinking\n"""
        if outputStatus == 0:  # Success
            self._blink("green", blinkFreq, blinkReps)
        elif outputStatus == 1:  # Fail
            self._blink("red", blinkFreq, blinkReps)
        else:  # Thinking / doing something else.
            self._blink("blue", blinkFreq, blinkReps)

# Example
a = LightControl(13, 12, 11)
a.lightNotification(0)
