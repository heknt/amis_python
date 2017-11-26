nums = []
amount_inp = int(input("amount of numbers: "))


def input_data(amount):
    """ APPENDING to LIST """
    if amount == 0:
        return nums
    nums.append(int(input("enter number: ")))
    return get_reverse(amount-1)


def get_reverse(rev_list):
    """ REVERSE LIST """
    rev_list.sort(reverse=True)
    return rev_list


print(get_reverse(input_data(amount_inp)))
