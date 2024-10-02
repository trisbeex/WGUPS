import datetime
import re
import logistics


#this class is loaded with packages to deliver
class Truck:

    csvReader = logistics.Logistics()

    def __init__(self, logistics, departureHours=8, departureMinutes=0):

        self.truck_bed = []
        self.packing_list = []
        self.currentAddressIndex = 0
        self.route_miles = 0
        self.route_hours = 0
        self.departureTime = datetime.timedelta(hours=int(departureHours), minutes=int(departureMinutes), seconds=int(0))
        self.currentTime = datetime.timedelta(hours=int(departureHours), minutes=int(departureMinutes), seconds=int(0))
        logistics.trucks.append(self)
        self.truck_number = len(logistics.trucks)


    #delivers the packages, updates, the status, and removes it from the truck, updates the current address of the truck as well as
    #its miles and active hours for the day
    def deliverPackage(self, currentAddressIndex, package, distance):
        self.route_miles = round(self.route_miles + distance, 2)
        self.route_hours = round(self.route_miles / 18.0, 2)
        #turns the hours into minutes to add to the time
        self.currentTime = self.currentTime + datetime.timedelta(minutes=(distance / 18.0) * 60)
        self.currentAddressIndex = currentAddressIndex
        package.deliverTime = self.currentTime
        package.status = f"Package {package.key} was delivered by Truck {self.truck_number} at {self.currentTime}"
        self.truck_bed.remove(package)



    #takes the package table and adds the package to the truck using its bucket
    def loadPackage(self, packageNums, packageTable):
        for packageNum in packageNums:
            self.truck_bed.append(packageTable[packageNum][0][1])
        self.packing_list = self.truck_bed.copy()

    #this method checks the truck departure time and the packages delivery time with a user provided time
    #to determine the status of the package
    def packageStatusAll(self, time):

        package_time_string = ""
        for package in self.packing_list:

            #if the truck hasn't left yet it's at the hub, if the package was delivered after the time requested
            #then it was in route, otherwise provide the delivery time
            if time < self.departureTime:

                #at the hub the package's address has not been updated yet
                if package.key == 9:
                    package.address = "300 State St"

                package.status = f"Package {package.key} is still at the hub"
                print(package)


                continue

            package_time_delta = package.deliverTime

            #if the provideD time is before the delivery time but after the departure time it is out for delivery
            if time >= self.departureTime and time < package_time_delta:

                # if the package is not at the hub and it is package 9 this address has been updated by the time it leaves
                if package.key == 9:
                    package.address = "410 S State St"

                package.status = f"Out for delivery on Truck {self.truck_number}"
                print(package)

            #if the other cases failed it was delivered
            else:

                # if the package is not at the hub and it is package 9 this address has been updated by the time it leaves
                if package.key == 9:
                    package.address = "410 S State St"

                package.status = f"Package {package.key} was delivered by Truck {self.truck_number} at {package_time_delta} "
                print(package)


    #returns the status of a single package
    def packageStatus(self, id, time):

        package_time_string = ""
        for package in self.packing_list:
            if package.key == id:

                # if the truck hasn't left yet it's at the hub, if the package was delivered after the time requested
                # then it was in route, otherwise provide the delivery time
                if time < self.departureTime:

                    # at the hub the package's address has not been updated yet
                    if package.key == 9:
                        package.address = "300 State St"

                    package.status = f"Package {package.key} is still at the hub"
                    print(package)
                    return True


                package_time_delta = package.deliverTime

                # if the provided time is before the delivery time but after the departure time it is out for delivery
                if time >= self.departureTime and time < package_time_delta:

                    # if the package is not at the hub and it is package 9 this address has been updated by the time it leaves
                    if package.key == 9:
                        package.address = "410 S State St"

                    package.status = f"Out for delivery on Truck {self.truck_number}"
                    print(package)

                # if the other cases failed it was delivered
                else:

                    # if the package is not at the hub and it is package 9 this address has been updated by the time it leaves
                    if package.key == 9:
                        package.address = "410 S State St"

                    package.status = f"Package {package.key} was delivered at {package_time_delta} by Truck {self.truck_number}"
                    print(package)
                return True

        return False







    #takes the current location of the truck and the location of the next package and returns the distance
    def returnToHub(self, distance):

        self.route_miles = round(self.route_miles + distance, 2)
        self.route_hours = round(self.route_miles / 18.0, 2)
        # turns the hours into minutes to add to the time
        self.currentTime = self.currentTime + datetime.timedelta(minutes=(distance / 18.0) * 60)
        self.currentAddressIndex = 0







