first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

if first_number > second_number:
    if second_number > third_number:
        print("\nThe smallest number is",third_number)
    elif second_number == third_number:
        print("\nThe smallest numbers is",second_number,
              "and",third_number)
    else:
        print("\nThe smallest number is",second_number)

elif first_number < second_number:
    if first_number > third_number:
        print("\nThe smallest number is",third_number)
    elif first_number == third_number:
        print("\nThe smallest numbers is",first_number,
              "and",third_number)
    else:
        print("\nThe smallest number is",first_number)

else:
    if first_number > third_number:
        print("\nThe smallest number is",third_number)
    elif first_number < third_number:
        print("\nThe smallest numbers is",first_number,
              "and",second_number)
    else:
        print("\nNumbers are equal")
