# Look where the information is stored or centered.  Lower coupling: Define the structure and group the code around that.  
# Higher cohension: they can only do one thing around each structure item.

import string
import random

class VehicleRegistry:
    # container for two helper methods
    # High coupling - changes will impact application.
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    # Problem does too many actions  (Low cohension and high coupling)

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # ** Move to VehicleRegistry
        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)
        # ** Move to VehicleRegistry
        
        # compute the catalogue price
        # hard to add new items.
        # Bad coupling: brand and price are tied together
        # A mixture of brand and vehicle instance information. (needs to be separated)
        # one brand
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        # hard to determine tax, it depends on being not electric/gas not brand
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")

app = Application()
app.register_vehicle("BMW 5")
