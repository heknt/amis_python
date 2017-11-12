error = True
while error:
    year = int(input("Enter value of years: "))
    if year > 0:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print("LEAP")
        else:
            print("COMMON")
        error = False
    else:
        print("Need a positive number")
