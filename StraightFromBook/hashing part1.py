class Plate:
    def __init__(self, CoS, CoC, EN):
        self.code_of_state = CoS
        self.code_of_city = CoC
        self.extra_nums = EN


    """def __hash__(self):
        string = self.GetPlate()
        return hash(string)"""
        

    def GetPlate(self):
        output = self.code_of_state + str(self.code_of_city) + str(self.extra_nums)
        return output
    
    """def __eq__(self, license_plate2):
        return self.GetPlate() == license_plate2.GetPlate()"""




if __name__ == "__main__":
    license_plate = Plate("YC", 11, 45)
    license_plate2 = Plate("YC", 11, 45)
    license_plate3 = Plate("TC", 3, 12)
 
    seeet = {Plate("YC", 11, 45), Plate("YC", 11, 45), Plate("YC", 11, 45)}
    for i in seeet:
        print(i.GetPlate())
    print("\n")
    dictionary = {license_plate : 1, license_plate2 : 2, license_plate3 : 3}

    for i in dictionary.keys():
        print(i.GetPlate())
    
