# structure-outline
# Note: this file does not run
# Remove dependency of turn on/turn off

# Add abc module to define a class as an abstract method.
from abc import ABC, abstractmethod # (4), 

# add ABC in method parameters to define class as abstract. (I)
# Note: abstract classes can not be an instance. (i.e.) s = Switchable() (II)
class Switchable(ABC): #(1), #(5) - ABC

    # Add an abstract notation.
    @abstractmethod #(6)
    def turn_on(self): #(2)
        pass

    # Add an abstract notation.
    @abstractmethod #(7)
    def turn_off(self): #(3)
        pass

# Instead inherit the abstract class by adding the class as a parameter (II)
class LightBulb(Switchable):

    # The abstract sub methods must be added to the LightBulb class
    # Else a TypeError is generated. 
    # This allows the programmer to track which classes are implemented.
    def turn_on(self):
        pass 

    def turn_off(self):
        pass

class Fan(Switchable):

    def turn_on(self):
        pass 

    def turn_off(self):
        pass


class ElectricPowerSwitch:

    # Now add the Switchable abstract method to the init method. (II)
    # Also change the name to reflect that this is no longer a light.
    def __init__(self, client: Switchable):
        pass 

    def press(self):
        pass

l = LightBulb()
f = Fan()
# change the object run when defining the switch.  (III)
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()