first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if first_number < second_number:
    print("The smallest number is", first_number)
elif first_number > second_number:
    print("The smallest number is", second_number)
else:
    print("Numbers are equal")
