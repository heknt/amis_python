error = True
while error:
    coord11 = int(input("Enter row of first cell: "))
    coord12 = int(input("Enter column of first cell: "))
    coord21 = int(input("Enter row of second cell: "))
    coord22 = int(input("Enter column of second cell: "))
    if (0 < coord11 < 9) and (0 < coord12 < 9) and (0 < coord21 < 9) and (0 < coord22 < 9):
        if (coord11 == coord21) or (coord12 == coord22):
            print("YES")
        elif (coord11 == coord21) and (coord12 == coord22):
            print("The rook isn't moving")
        else:
            print("NO")
        error = False
    else:
        print("\nNeed a true coordinates")
