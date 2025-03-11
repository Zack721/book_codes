def HashFunction(user_input):
    #result = 0
    final_list = []
    for element in user_input:
        if element.isnumeric() == False:
           element = ord(element)
        final_list.append(str(element))

    final_hash_val = "".join(final_list)
    return int(final_hash_val)

if __name__ == "__main__":
    hash_value = HashFunction(input("Value please: \n"))
    print(hash_value)

