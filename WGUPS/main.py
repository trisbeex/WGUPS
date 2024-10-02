#Tristan Barona
#Student ID: 011834217
#C950 Data Structure & Algorithms II WGUPS Routing Program

import truck
import hashmap
import packages
import logistics
import datetime


#create a table of packages and read the address, packages, and distances into the program
hashTable = hashmap.HashTable()
logistics = logistics.Logistics()
logistics.readpackageinfo(hashTable)
logistics.readaddressinfo()
logistics.readdistanceinfo()

#create 3 trucks for the deliveries and add their packages, in this case, the trucks are manually loaded
truck1 = truck.Truck(logistics)
truck2 = truck.Truck(logistics, departureHours=10, departureMinutes=20)
truck3 = truck.Truck(logistics, departureHours=9, departureMinutes=5)


packingList1 = [7, 10, 14, 15, 16, 19, 20, 21, 29, 30, 34, 37]
truck1.loadPackage(packingList1, hashTable.table)

#leaves last after 10:20
packingList2 = [3, 5, 8, 9, 11, 17, 18, 22, 23, 31, 32, 36, 38]
truck2.loadPackage(packingList2, hashTable.table)

#package 0 is 40
#leaves at 9:05
packingList3 = [1, 2, 4, 6, 12, 13, 24, 25, 26, 27, 28, 33, 35, 39, 0]
truck3.loadPackage(packingList3, hashTable.table)

#perform the deliveries


print("||        ||      ||")
print(" ||     || ||    ||")
print("  ||  ||    ||  ||")
print("    ||        ||")

print("Welcome to the WGUPS Package Tracker!")
user_input = ""


while True:
    logistics.truckCount = 3
    logistics.deliverPackages(truck1)
    logistics.deliverPackages(truck2)

    print("\nPlease enter the time of day you'd like to track by typing the time using the 'HH:MM' format using 24 hour "
          "time.")
    print("You can also type 'total' for all package status and the total mileage of trucks for the day.")
    print("Type 'exit' to exit.")
    user_input = input()

    if user_input.lower() == "exit":
        break

    elif user_input.lower() == "total":
        logistics.getDailyTotal()

    else:
        try:
            #parse the user's string and convert to a timedelta object
            user_time = user_input.split(':')

            #if the user doesn't provide the 2 digit hour we'll help them by padding a zero
            user_time[0] = user_time[0].zfill(2)
            user_time_delta = datetime.timedelta(hours=int(user_time[0]), minutes=int(user_time[1]), seconds=int(0))


        except ValueError as e:
            print(f"Invalid input {e}. Please enter a valid value in the format of HH:MM, Ex. 04:25")
            continue

        print("To track a specific package enter its ID, otherwise enter 'All.'")
        user_input_package = input()

        if user_input_package.lower() == 'all':
            for truck in logistics.trucks:
                truck.packageStatusAll(user_time_delta)
        else:

            try:
                package_number = int(user_input_package)
                package_found = False
                for truck in logistics.trucks:
                    package_found = truck.packageStatus(package_number, user_time_delta)

                    if package_found:
                        break

                if not package_found:
                    print("Package ID was not found.")


            except ValueError:
                print("Invalid input. Please enter a package ID or 'All'.")








