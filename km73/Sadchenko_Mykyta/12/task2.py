def f_max(nums):
    """
    This function is determines the maximum of list.

    Args:
        nums - list of positive integer numbers
        maxim - maximum of list
    Returns:
        maxim or int(nums[0]) - maximum of list
    Raises:
        ValueError
        OverflowError
        IndexError
    """
    if len(nums) == 1:
        return int(nums[0])
    maxim = f_max(nums[1:])
    return maxim if maxim >= int(nums[0]) else int(nums[0])


def f_count_max(length, maximum):
    """
    This function is determines the maximum of list.

    Args:
        numb - list of positive integer numbers
        amount_max - value of maximums of list
        length - length of list
    Returns:
        amount_max - value of maximums of list
    Raises:
        OverflowError
        IndexError
    """
    global amount_max,  numb
    if length == 0:
        return amount_max
    if int(numb[length-1]) == maximum:
        amount_max += 1
    return f_count_max(length-1, maximum)


def validation(chars):
    """
    This function is checking data(data must be positive integer, should contain at least one number).

    Args:
        chars - characters, that will be testing
    Returns:
        chars - positive integer
    Raises:
        ValueError
    Examples:
        >>> print(validation('4 5 6 7'))
        ['4', '5', '6', '7']
        >>> print(validation('a 2 2 3'))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if len(chars.split()) == 0:
        return validation(input("at least one number!: "))
    elif set(chars).issubset(' 0123456789'):
        return chars.split()
    return validation(input("natural!: "))


def test_validation():
    """
    This function is testing function 'validation'

    Args:
        Function takes no args
    Returns:
        None
    Raises:
        AssertionError
    """
    assert validation('4 5 6 7') == ['4', '5', '6', '7']
    assert validation('7 0 9 123 929 1') == ['7', '0', '9', '123', '929', '1']
    assert validation('123') == ['123']
    return


amount_max = 0
numb = validation(input("enter numbers: "))
test_validation()
print("amount of max-numbers:", f_count_max(len(numb), f_max(numb)))
