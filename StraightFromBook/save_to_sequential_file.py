# sequential file handling Task 26.01
import pickle  # this library is required to create binary files
from datetime import date

MAXCARS = 10

class CarRecord:
    def __init__(self):
        self.VehicleID = "dummy"
        self.Registration = ""
        self.DateOfRegistration = date(1990, 1, 1)
        self.EngineSize = 0
        self.PurchasePrice = 0.00

def SaveData(Car):
    # file channel for car records
    with open('CarFile.DAT', 'wb') as CarFile:  # open file for binary write
        for i in range(MAXCARS + 1):  # loop for each array element
            # write a whole record to the binary file
            pickle.dump(Car[i], CarFile)

def LoadData():
    Car = []  # start with empty list
    try:
        with open('CarFile.DAT', 'rb') as CarFile:  # open file for binary read
            EoF = False
            while not EoF:  # check for end of file
                try:
                    Car.append(pickle.load(CarFile))  # append record from file to end of list
                except EOFError:
                    EoF = True
    except FileNotFoundError:
        print("File not found. Starting with an empty record list.")
    
    return Car

def OutputRecords(Car):
    for i in range(1, MAXCARS + 1):  # loop for each array element
        print(Car[i].VehicleID)  # show one field

def AddRecords(Car):
    i = int(input('Record Number? '))
    while i != 0:
        Car[i].VehicleID = input('Vehicle ID: ')
        Car[i].Registration = input('Registration: ')
        Car[i].DateOfRegistration = input('Registration Date: ')
        Car[i].EngineSize = int(input('Engine size: '))
        Car[i].PurchasePrice = float(input('Purchase price: '))
        i = int(input('Next Record Number? '))
    return Car

def main():
    Car = [CarRecord() for i in range(MAXCARS + 1)]  # only run this 1st time
    SaveData(Car)  # only run this first time
    Car = LoadData()  # from existing file
    OutputRecords(Car)
    Car = AddRecords(Car)
    OutputRecords(Car)
    SaveData(Car)

main()
