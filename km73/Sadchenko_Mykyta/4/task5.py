first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number == second_number:
    if second_number == third_number:
        result = 3
    else:
        result = 2
elif second_number == third_number:
    result = 2
elif first_number == third_number:
    result = 2
else:
    result = 0

print(result)
