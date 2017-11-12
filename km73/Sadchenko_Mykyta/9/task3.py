def power(b, n):
    if n == 0:
        return 1
    else:
        return b*power(b, n-1)


x = float(input("b: "))
y = int(input("n: "))
print(power(x, y))
