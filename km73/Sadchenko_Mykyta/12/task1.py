def f_max1(nums):
    """
    This function is determines the maximum of list.

    Args:
        nums - list of positive integer numbers
        max1 - maximum of list
    Returns:
        max1 or int(nums[0]) - maximum of list
    Raises:
        ValueError
        OverflowError
        IndexError
    """
    if len(nums) == 2:
        return int(nums[0]) if int(nums[0]) >= int(nums[1]) else int(nums[1])
    max1 = f_max1(nums[1:])
    return max1 if max1 >= int(nums[0]) else int(nums[0])


def f_max2(nums):
    """
    This function is determines the maximum of list.

    Args:
        nums - list of positive integer numbers
        max2 - maximum of list
    Returns:
        max2 or int(nums[0]) - maximum of list
    Raises:
        ValueError
        OverflowError
        IndexError
    """
    if len(nums) == 1:
        return int(nums[0])
    max2 = f_max2(nums[1:])
    return max2 if max2 >= int(nums[0]) else int(nums[0])


def validation(chars):
    """
    This function is checking data(data must be positive integer, should contain at least two numbers).

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
    if len(chars.split()) < 2:
        return validation(input("at least two numbers!: "))
    elif set(chars).issubset(' 0123456789'):
        return chars.split()
    return validation(input("natural!: "))


def removing(counted):
    """
    This function removes maximum from list.

    Args:
        counted - value of maximums of list
        numb - list of positive integer numbers
        maximum - maximum of list
    Returns:
        numb - modified list (deleted maximum)
    Raises:
        OverflowError
        IndexError
    """
    global maximum, numb
    if counted == 0:
        return numb
    m = numb.index(maximum)
    numb = numb[:m] + numb[m+1:]
    return removing(counted-1)


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


numb = validation(input("enter numbers: "))
maximum = str(f_max1(numb))
test_validation()
print("second maximum:", f_max2(removing(numb.count(maximum))))
