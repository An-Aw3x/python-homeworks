from abc import ABC, abstractmethod
from collections import deque

class Driver: # Deonstrates SRP, as driver class is only really responsible for the name of the driver
    def __init__(self, name):
        self.name = name

class Customer(ABC): # OCP is used here, as Customer is an abstract class that can be extended by other classes without modifying it
    def __init__(self, name, pickup_location, dropoff_location, distance, driver=None): # SRP is also used here
        self.name = name
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.distance = distance
        self.driver = driver # ISP is used as Customer is Abstract. Only Child classes implement the methods they need
    
    @abstractmethod
    def get_fare(self):
        pass

class RideService:
    def __init__(self):
        self.drivers = deque() 

    def add_driver(self, driver):
        self.drivers.append(driver)  

    def assign_driver(self, customer):
        if not self.drivers:
            return "No drivers available"
        customer.driver = self.drivers.popleft()  
        return f"Ride fare: {customer.get_fare()}, driver: {customer.driver.name}"
    
class LuxuryCustomer(Customer): # all the Child classes use LSP as they are Used Interchangeably with the parent class Customer without messing up the code.
    def get_fare(self):
        return self.distance * 10 # and ISP, all the child classes only implement methods relevant to them

class EconomyCustomer(Customer):
    def get_fare(self):
        return self.distance * 5

class PoolCustomer(Customer):
    def get_fare(self):
        return self.distance * 3
    

def drivers():
    list_of_drivers = RideService()
    list_of_drivers.add_driver(Driver("Alice"))
    list_of_drivers.add_driver(Driver("Bob"))
    return list_of_drivers

def main():
    ride_service = drivers()
    
    customer1 = EconomyCustomer("John", "Airport", "Downtown", 15)
    customer2 = LuxuryCustomer("Rebecca", "College", "Downtown", 10)
    customer3 = PoolCustomer("Mike", "Downtown", "Shopping Mall", 5) # Sorry Mike, no driver for you
    print("Welcome to SwiftRide!")
    print(ride_service.assign_driver(customer1))
    print(ride_service.assign_driver(customer2))
    print(ride_service.assign_driver(customer3))
    return

if __name__ == "__main__":
    main()



   