# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:04:56 2020

@author: orhunyildiz
"""
import datetime
class VehicleRent:
    
    def __init__(self, stock):
        self.stock = stock
        self.now = 0
        
    def displayStock(self):
        print("{} vehicle(s) available to rent.".format(self.stock))
        return self.stock
    
    def rentHourly(self, n):
        if n <= 0:
            print("Number should be positive!")
            return None
        elif n > self.stock:
            print("Sorry {} vehicle(s) available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) for hourly at {} hours.".format(n, self.now.hour))
            self.stock -= n
            return self.now
            
    def rentDaily(self, n):
        if n <= 0:
            print("Number should be positive!")
            return None
        elif n > self.stock:
            print("Sorry {} vehicle(s) available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) for daily at {} hours.".format(n, self.now.hour))
            self.stock -= n
            return self.now
        
    def returnVehicle(self, request, brand):
        carHPrice = 10
        carDPrice = carHPrice * 8 / 10 * 24
        bikeHPrice = 5
        bikeDPrice = bikeHPrice * 7 / 10 * 24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds / 3600 * carHPrice * numOfVehicle
                elif rentalBasis == 2: #♠ daily
                    bill = rentalPeriod.seconds / (3600 * 24) * carDPrice * numOfVehicle
                
                if numOfVehicle >= 2:
                    print("You have an extra 20% discount!")
                    bill *= 0.8
                    
                print("Thank you for returning your car!")
                print("Price: {}$".format(bill))
                
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds / 3600 * bikeHPrice * numOfVehicle
                elif rentalBasis == 2: #♠ daily
                    bill = rentalPeriod.seconds / (3600 * 24) * bikeDPrice * numOfVehicle
                
                if numOfVehicle >= 4:
                    print("You have an extra 20% discount!")
                    bill *= 0.8
                    
                print("Thank you for returning your bike!")
                print("Price: {}$".format(bill))
                
        else:
            print("You do not rent a vehicle!")
            return None


class CarRent(VehicleRent):
    
    global discountRate
    discountRate = 15
    
    def __init__(self, stock):
        super().__init__(stock)
    
    def discount(self, b):
        bill = b - (b * discountRate) / 100
        return bill

class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)


class Customer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasisB = 0
        self.rentalTimeB = 0
        self.cars = 0
        self.rentalBasisC = 0
        self.rentalTimeC = 0
        
    
    def requestVehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you rent: ")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Input must be a number!")
                return -1
            
            if bikes < 1:
                print("Number of bikes should be greater than zero!")
                return -1
            else:
                self.bikes = bikes
            return self.bikes
        elif brand == "car":
            cars = input("How many cars would you rent: ")
            
            try:
                cars = int(cars)
            except ValueError:
                print("Input must be a number!")
                return -1
            
            if cars < 1:
                print("Number of cars should be greater than zero!")
                return -1
            else:
                self.cars = cars
            return self.cars
        else:
            print("Request vehicle error!")
    
    def returnVehicle(self, brand):
        if brand == "bike":
            if self.rentalTimeB and self.rentalBasisB and self.bikes:
                return self.rentalTimeB, self.rentalBasisB, self.bikes
            else:
                return 0,0,0
        elif brand == "car":
            if self.rentalTimeC and self.rentalBasisC and self.cars:
                return self.rentalTimeC, self.rentalBasisC, self.cars
        else:
            print("Return vehicle error!")