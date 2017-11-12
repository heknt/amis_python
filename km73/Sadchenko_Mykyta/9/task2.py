def power(a, n):
    result = 1
    for i in range(abs(n)):
        if n >= 0:
            result *= a
        else:
            result /= a
    return round(result, 3)


a_number = float(input("a: "))
n_power = int(input("n: "))
print(power(a_number, n_power))
