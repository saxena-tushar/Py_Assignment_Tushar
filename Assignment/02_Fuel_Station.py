'''Problem #2 - Fuel Station Design
Design a fuel station for 3 types of vehicles - Diesel, Petrol, and Electric. There are a fixed number of spots for each type of vehicle at the fuel station.

Implement the FuelStation class:
•	FuelStation(int diesel, int petrol, int electric) creates a  FuelStation object. The number of spots for each type of fuel is defined by the values provided to the constructor.
•	bool fuel_vehicle(str fuel_type)looks up whether there is an open slot that can provide fuel_type. A vehicle can only be fueled in a slot space of its fuel_type. If there is no slot free, return false, else put the vehicle in that fuel slot and return true.
•	bool open_fuel_slot(str fuel_type)releases a fuel slot of fuel_type so that another vehicle can be fueled. If you try to open a fuel slot, when all slots of a fuel_type are empty, return false. Otherwise, return true.
'''


class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int) -> None:
        self.total_spots = {
            'diesel': diesel,
            'petrol': petrol,
            'electric': electric
        }
        self.current_spots = {
            'diesel': diesel,
            'petrol': petrol,
            'electric': electric
        }

    def refuel_vehicle(self, fuel_type: str) -> bool:
        if self.current_spots[fuel_type] > 0:
            self.current_spots[fuel_type] -= 1
            return True
        return False

    def release_spot(self, fuel_type: str) -> bool:
        if self.current_spots[fuel_type] < self.total_spots[fuel_type]:
            self.current_spots[fuel_type] += 1
            return True
        return False


def main():
    fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

    operations = [
        ("refuel_vehicle", "diesel"),
        ("refuel_vehicle", "petrol"),
        ("refuel_vehicle", "diesel"),
        ("refuel_vehicle", "electric"),
        ("refuel_vehicle", "diesel"),
        ("release_spot", "diesel"),
        ("refuel_vehicle", "diesel"),
        ("release_spot", "electric"),
        ("release_spot", "electric")
    ]

    results = []
    for operation, fuel_type in operations:
        if operation == "refuel_vehicle":
            result = fuel_station.refuel_vehicle(fuel_type)
        elif operation == "release_spot":
            result = fuel_station.release_spot(fuel_type)
        results.append(result)

    print(results)


if __name__ == "__main__":
    main()
