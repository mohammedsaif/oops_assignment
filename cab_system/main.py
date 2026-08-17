from car import Car
from bike import Bike

car1 = Car("KA 0304589","toyoto","Raju",20)
car2 = Car("KA 0408954","Hyndai","saju",18)
bike1 = Bike("KA 0408954","honda","raghu",13)
bike2 = Bike("KA 0895625","honda","bojjapa",14)

vehicles = [car1,car2,bike1,bike2]

def display_vehicles():
    print("++++++++")
    print("Available vehicles")

    for index,vehicle in enumerate(vehicles,start = 1):
                print(
            f"{index}. {vehicle.vehicle_type()} - "
            f"{vehicle.vehicle_number} - "
            f"{vehicle.brand}"
        )
                print(f"   Driver : {vehicle.driver}")
                print(f"   Rate   : ₹{vehicle.price_per_km}/KM")
                print()

def calculate_trip_fares():
    trips = [
        (car1, 12),
        (car2, 25.5),
        (bike1, 8),
        (bike2, 15),
    ]

    print("\n---------------------------")
    print("Multiple Trip Fares")
    print("---------------------------")
    total = 0
    for vehicle, distance in trips:
        fare = vehicle.calculate_fare(distance)
        total += fare
        print(
            f"{vehicle.vehicle_type()} ({vehicle.brand}, {vehicle.vehicle_number}) - "
            f"{distance} KM - ₹{fare}"
        )
    print("---------------------------")
    print(f"Total Fare for All Trips: ₹{total}")
    print("---------------------------")


def book_cab():
    print("++++++ cab booking system");
    print("")
    display_vehicles()
    try:
        choice = int(input("choose the Select Vehicle:"))
        if choice <1 or choice > len(vehicles):
           print("Invalid vehicle selection.")
           return
        distance = float(input("enter the distance"))
        if distance <= 0:
            print("Distance must be greater than zero.")
            return
        selected_vehicle = vehicles[choice - 1]
        fare = selected_vehicle.calculate_fare(distance)
        print("\n---------------------------")
        print("Booking Details")
        print("---------------------------")

        print("Driver       :", selected_vehicle.driver)
        print("Vehicle      :", selected_vehicle.vehicle_type())
        print("Brand        :", selected_vehicle.brand)
        print("Vehicle No.  :", selected_vehicle.vehicle_number)
        print("Distance     :", distance, "KM")
        print("Rate         :", f"₹{selected_vehicle.price_per_km}/KM")
        print("Total Fare   :", f"₹{fare}")

        print("---------------------------")
    except ValueError:
        print("Please enter a valid number.")


def main():
     print("================================")
     print("       CAB BOOKING SYSTEM")
     print("================================")
     while True:

        print("\n1. Book Cab")
        print("2. Calculate Fares for Multiple Trips")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_cab()

        elif choice == "2":
            calculate_trip_fares()

        elif choice == "3":
            print("Thank you for using Cab Booking System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main();


        
                