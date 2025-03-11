def HashFunction(user_input):
    list_of_val = []
    final_list = []
    for i in user_input:
        list_of_val.append(i)

    for element in list_of_val:
        if element.isnumeric() == False:
           element = ord(element)
        final_list.append(str(element))

    final_hash_val = "".join(final_list)
    return int(final_hash_val)


if __name__ == "__main__":
    hash_value = HashFunction(input("Value please"))
    """print(type(hash_value))"""
    print(chr(33))












"""def HashFunction(user_input):
    result = 0

    for element in user_input:
        if element.isnumeric() == False:
           element = ord(element)
        final_list.append(str(element))

    final_hash_val = "".join(final_list)
    return int(final_hash_val)

if __name__ == "__main__":
    hash_value = HashFunction(input("Value please"))
    print(hash_value)"""