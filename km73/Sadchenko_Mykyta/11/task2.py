nums = []
amount_inp = int(input("amount of numbers: "))


def input_data(amount):
    """ APPENDING to LIST """
    if amount == 0:
        return nums
    nums.append(int(input("enter number: ")))
    return input_data(amount-1)


def min_num(char_list):
    """ FIND MINIMAL ELEMENT """
    return min(char_list)


print(min_num(input_data(amount_inp)))
