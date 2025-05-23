import random

print('Fahrzeugdetails')
print('')

# Attribute values

colors = ['blau', 'rot', 'grün', 'schwarz', 'weiß', 'gelb', 'grau']
sizes = ['klein', 'mittel', 'groß']
door_counts = ['2Türen', '3Türen', '4Türen', '5Türen']
fuel_types = ['Benzin', 'Diesel', 'Elektro', 'Hybrid']
vehicle_types = ['PKW', 'Lkw', 'SUV', 'Van', 'Cabrio']
drive_types = ['Front', 'Heck', 'AWD']
build_types = ['Frontmotor', 'Heckmotor', 'Mittelmotor']
trans_types = ['Automatik', 'Manuell']
rim_types= ['Stahl', 'Aluminium', 'Carbon']
wheel_types= ['Sommer', 'Winter', 'Allwetter']

# Vehicle class with English variable names

class Vehicle:
    def __init__(self, color, size, doors, fuel, vtype, drive, build, trans, rim, wheel):
        self.color = color
        self.size = size
        self.doors = doors
        self.fuel = fuel
        self.vtype = vtype
        self.drive = drive
        self.build = build
        self.trans = trans
        self.rim = rim
        self.wheel = wheel

    def display(self):
        return f"Farbe: {self.color}, Größe: {self.size}, Türen: {self.doors}, Kraftstoff: {self.fuel}, Typ: {self.vtype}, Antrieb: {self.drive}, Bauweise: {self.build}, Getriebe: {self.trans}, Felgen: {self.rim}, Bereifung: {self.wheel}"

# First vehicle with fixed values

vehicles = [Vehicle('blau', 'groß', '3Türen', 'Diesel', 'Lkw', 'Front', 'Frontmotor', 'Automatik', 'Stahl', 'Sommer')]

# Additional vehicles with random attributes

for _ in range(6):
    vehicle = Vehicle(
        color=random.choice(colors),
        size=random.choice(sizes),
        doors=random.choice(door_counts),
        fuel=random.choice(fuel_types),
        vtype=random.choice(vehicle_types),
        drive=random.choice(drive_types),
        build=random.choice(build_types),
        trans=random.choice(trans_types),
        rim=random.choice(rim_types),
        wheel=random.choice(wheel_types)

    )
    vehicles.append(vehicle)

# for Schleife (um alle Fahrzeuge zu beeinflussen)

for vehicle in vehicles:
    vehicle.color, vehicle.size = vehicle.size, vehicle.color

# Print all vehicle details

for i, vehicle in enumerate(vehicles, start=1):
    print(f"Fahrzeug {i}: {vehicle.display()}")