import datetime

class Package:
    def __init__(self, pid, address, city, zipcode, deadline, weight, status ):
        self.key = pid
        self.address = address
        self.city = city
        self.zip = zipcode
        self. deadline = deadline
        self.weight = weight
        self.deliverTime = datetime.timedelta(hours=int(0), minutes=int(0), seconds=int(0))
        self.status = status



    def __str__(self):
        return (f"PID: {self.key}, "
              f"Address: {self.address}, "
              f"City: {self.city}, "
              f"Zip: {self.zip}, "
              f"Weight: {self.weight}, "
              f"Deliver By: "
              f"{self.deadline}), "
              f"Status: {self.status}")

    def __repr__(self):
        return (f"PID: {self.key}, "
              f"Address: {self.address}, "
              f"City: {self.city}, "
              f"Zip: {self.zip}, "
              f"Weight: {self.weight}, "
              f"Deliver By: "
              f"{self.deadline}), "
              f"Status: {self.status}")








