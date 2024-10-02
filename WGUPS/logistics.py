import csv
import datetime
import packages
import hashmap



class Logistics:

    def __init__(self):

        self.trucks = []
        self.truckCount = 3
        self.distanceArray = []
        self.addressArray = []
        self.totalMiles = 0
        self.total_hours = 0


    #retrieves the package information from a csv then adds it to a provided hashtable
    def readpackageinfo(self, hashtable):
        with open('package.csv', mode='r') as file:
            packagefile = csv.reader(file, delimiter=",")
            #ignores the header
            next(packagefile)
            for package in packagefile:
                pid = int(package[0])
                address = package[1]
                city = package[2]
                zipcode = package[4]
                deadline = package[5]
                weight = int(package[6])
                status = "Not Delivered"

                package = packages.Package(pid, address, city, zipcode, deadline, weight, status)

                hashtable.add_package(pid, package)


    #retrieves distance information from a csv
    def readdistanceinfo(self):
        with open('distance.csv', mode='r') as file:
            distanceFile = csv.reader(file, delimiter=",")

            for destination in distanceFile:
                self.distanceArray.append(destination)
                #print(destination)
            #return self.distanceArray

    #retrieves package address information from a csv
    def readaddressinfo(self):
        with open('address.csv', mode='r') as file:
            addressFile = csv.reader(file, delimiter=",")

            for address in addressFile:
                self.addressArray.append(address)
                #print(addressFile)

            #return self.addressArray

    #takes the current location of the truck and the location of the next package and returns the distance
    def getDistance(self, startIndex, package):
        destinationAddress = package.address

        for address in self.addressArray:
            #pulls the index of the destination address that matches with the distance array if there's a match
            if destinationAddress in address:
                addressIndex = int(address[0])

        #because the distance list populates new areas as it goes further down the row
        #searching for lower index than the destination will return none

        if (addressIndex > startIndex):
            distance = self.distanceArray[addressIndex][startIndex]
        else:
            distance = self.distanceArray[startIndex][addressIndex]

        return float(distance)

    def getDistanceToHub(self, startIndex):
        return float(self.distanceArray[startIndex][0])

    #takes the address of the package and returns the index of it from the address list
    def getAddressIndex(self, package):
        destinationAddress = package.address

        for address in self.addressArray:
            #pulls the index of the destination address that matches with the distance array if there's a match
            if destinationAddress in address:
                addressIndex = int(address[0])
                return addressIndex

    # the deliverPackages method/algorithm takes a truck and iterates through the package addresses to determine which
    # delivery address is the closest from the current address, once found the package is delivered, and the truck is updated
    # this continues until the truck has delivered all of its packages
    def deliverPackages(self, truck):

        # trucks needing to be dispatched goes down by 1
        self.truckCount -= 1

        for package in truck.truck_bed:
            package.status = "Out for Delivery"

        # initialize variables for loop
        nearestDistance = 999.0
        nextPackage = 0

        while len(truck.truck_bed) > 0:

            for package in truck.truck_bed:

                # this method returns the distance from the current package's location and updates the closest package
                # if it is less than the least previous value
                curPackageDistance = self.getDistance(truck.currentAddressIndex, package)

                if curPackageDistance < nearestDistance:
                    nearestDistance = curPackageDistance
                    nextPackage = package

            # once the shortest destination is found, the address index is obtained and the truck is updated
            newAddressIndex = self.getAddressIndex(nextPackage)
            truck.deliverPackage(newAddressIndex, nextPackage, nearestDistance)


            nearestDistance = 999.0

        # if there are still trucks that need to be dispatched the next available driver needs to return to the hub and
        # complete the next route
        # since there are 2 drivers, the next truck they'll take will always be two away from the current index
        # (the other driver takes the one inbetween) if it is out of bounds the driver is done
        if self.truckCount > 0 and not self.trucks.index(truck) + 2 >= len(self.trucks) :

            truck.returnToHub(self.getDistanceToHub(truck.currentAddressIndex))
            self.trucks[self.trucks.index(truck) + 2].departureTime = truck.currentTime
            self.trucks[self.trucks.index(truck) + 2].currentTime = truck.currentTime
            self.deliverPackages(self.trucks[self.trucks.index(truck) + 2])

    #takes the current location of the truck and the location of the next package and returns the distance
    def returnToHub(self, startIndex, truck):
        distance = self.distanceArray[startIndex][0]
        truck.route_miles = round(truck.route_miles + distance, 2)
        truck.route_hours = round(truck.route_miles / 18.0, 2)
        # turns the hours into minutes to add to the time
        truck.currentTime = truck.currentTime + datetime.timedelta(minutes=(distance / 18.0) * 60)
        truck.currentAddressIndex = 0

        return float(distance)

    def getDailyTotal(self):

        totalMiles = 0
        totalHours = 0

        for truck in self.trucks:
            totalMiles += truck.route_miles
            totalHours += truck.route_hours
            totalMiles = round(totalMiles, 2)
            totalHours = round(totalHours, 2)

        print(f"The Total Mileage for Today's Routes is: {totalMiles}")
        print(f"The Total Time Spent Making Deliveries is: {totalHours} hours")






