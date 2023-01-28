# structure-outline
# Note: this file does not run

import string
import random

# Actions
# Create an class for the tax information and a class for an instance of the vehicle created
# Add a method that works and is associated with that data.

# Note each function is only a few lines of code.

# high level information
class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    # Add initializer

    # Add method that computes the tax and returns tax (or one for each)

    # Print method for information

# instance
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    # Add initializer

    # Print method for information - calls print for VehicleInfo

class VehicleRegistry:

    vehicle_info = { }

    def add_vehicle_info(self, brand, electric, catalogue_price):
        # Looks up info in VehicleInfo
        pass

    def __init__(self):
        # Call information here
        pass

    # Modify code so the actions are here not in the Application
    def generate_vehicle_id(self, length):
        pass

    def generate_vehicle_license(self, id):
        pass
    
    # Make this function create an instance of Vehicle
    def create_vehicle(self):
        pass

class Application:

    def register_vehicle(self, brand: string):
        # returns the registered vehicle
        pass
    
# Run the app
# Save the registered instance of a vehicle
# Print the Vehicle (give the user a reciept)