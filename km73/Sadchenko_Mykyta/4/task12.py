error = True
while error:
    n = int(input("Enter value of row: "))
    m = int(input("Enter value of column: "))
    k = int(input("Enter rest of cells: "))
    d = n * m    # amount of cells
    if (n > 0) and (m > 0) and (k > 0):
        if ((d % k) % n == 0) or ((d % k) % m == 0):
            print("YES")
        else:
            print("NO")
        error = False
    else:
        print("\nEnter positive numbers")
