class Plate:
    def __init__(self, CoS, CoC, EN):
        self.code_of_state = CoS
        self.code_of_city = CoC
        self.extra_nums = EN


    def __hash__(self):
        user_input = self.code_of_state + str(self.code_of_city) + str(self.extra_nums)
        final_list = []
        for element in user_input:
            if element.isnumeric() == False:
                element = ord(element)
            final_list.append(str(element))

        final_hash_val = "".join(final_list)
        return int(final_hash_val)

    def GetPlate(self):
        output = self.code_of_state + str(self.code_of_city) + str(self.extra_nums)
        return output

    """ def __eq__(self, other):
       return other.code_of_state == self.code_of_state and other.code_of_city == self.code_of_city and other.extra_nums == self.extra_nums
    """
class NoDuplicates:
    def __init__(self):
        self.list = []


    def Insert(self, value):
        if value not in self.list:
            self.list.append(value) 


    def Print(self):
        for i in self.list:
            print(i)

if __name__ == "__main__":
    """ license_plate = Plate("YC", 11, 45)
        license_plate2 = Plate("YC", 11, 45)
        license_plate3 = Plate("TC", 3, 12)
        dictionary = {license_plate : 1, license_plate2 : 2, license_plate3 : 3}

        for i in dictionary.keys():
            print(i.GetPlate())

        print("Now for the set stuff \n")
        seeet = {Plate("YC", 11, 45), Plate("YC", 11, 45), Plate("YC", 11, 45)}
        for i in seeet:
            print(i.GetPlate())"""

    no_dups = NoDuplicates()


    license_plate = Plate("YC", 11, 45)
    license_plate2 = Plate("YC", 11, 45)
    license_plate3 = Plate("TC", 3, 12)

    no_dups.Insert(license_plate)
    no_dups.Insert(license_plate2)
    no_dups.Insert(license_plate3)
    no_dups.Print()
    