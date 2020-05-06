from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    # car_type = input("Car Type")
    # car_fuel = int(input("How Much Fuel Do We Have?"))
    # car_fanciness = int(input("How Fancy is the car?"))
    # taxi = SilverServiceTaxi(car_type, car_fuel, car_fanciness)
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()