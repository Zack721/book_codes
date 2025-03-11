class student:
    def __init__(self, full_name, age ,grade):
        self.full_name_ = full_name
        self.age_ = age
        self.grade_ = grade
    
    def __hash__(self):
        return hash(self.full_name_) % 10 + hash(self.age_) % 10 + hash(self.grade_) % 10

    def __eq__(self, other):
        return self.full_name_ == other.full_name_ and self.age_ == other.age_ and self.age_ == other.age_
    
    


if __name__ == "__main__":
    dictionary = {student("Isaac Ben Akan Taylor", 18, 12): 1, student("Josias", 23, 3): 2, student("Isaac Ben Akan Taylor", 18, 12): 3}
    for i in dictionary:
        print(i)
