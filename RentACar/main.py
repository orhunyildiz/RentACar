# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:31:53 2020

@author: orhunyildiz
"""
from rent import BikeRent, CarRent, Customer

bike = BikeRent(100)
car = CarRent(50)
customer = Customer()

mainMenu = True

while True:
    if mainMenu:
        print("""
              ***** Vehicle Rental Shop *****
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        
        mainMenu = False
        choice = input("Make Your Choice :) : ")
        
    if choice == "A" or choice == "a":
        print("""
              ***** Bike Menu *****
              1. Display Available Bikes
              2. Request a Bike on Hourly Basis (5$)
              3. Request a Bike on Daily Basis (84$)
              4. Return a Bike
              5. Main Menu
              6. Exit
              """)
        
        choice = input("Make Your Choice :) : ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It's not an integer!")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTimeB = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasisB = 1
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 3:
            customer.rentalTimeB = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasisB = 2
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasisB, customer.rentalTimeB, customer.bikes = 0, 0, 0
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 5:
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 6:
            break
        else:
            print("Invalid Input! Please enter a number between 1 - 6")
            mainMenu = True
            
    elif choice == "B" or choice == "b":
        print("""
              ***** Car Menu *****
              1. Display Available Cars
              2. Request a Car on Hourly Basis (10$)
              3. Request a Car on Daily Basis (192$)
              4. Return a Car
              5. Main Menu
              6. Exit
              """)
        choice = input("Make Your Choice :) : ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It's not an integer!")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
        elif choice == 2:
            customer.rentalTimeC = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasisC = 1
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 3:
            customer.rentalTimeC = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasisC = 2
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"), "car")
            customer.rentalBasisC, customer.rentalTimeC, customer.cars = 0, 0, 0
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 5:
            mainMenu = True
            print("||||||||||||||||||||||||")
        elif choice == 6:
            break
        else:
            print("Invalid Input! Please enter a number between 1 - 6")
            mainMenu = True
    
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Invalid Input! Please enter A, B or Q!")
        mainMenu = True
    
print("Thank you for using the Rental Vehicle Shop! Have a nice day!")
    