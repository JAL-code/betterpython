# SOLID = D: Dependency Inversion
# Abstract Base Class: MyPI - static checking
# Abstraction: Separate the description/definition of the interface from the actual implementation
# List of types


class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:
    # The problem with this program is that ElectricPowerSwitch is dependent on LightBulb
    def __init__(self, l: LightBulb): # last argument in parameter
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
