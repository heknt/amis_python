all_minutes = int(input("Enter number of minutes: "))
hours = (all_minutes//60) % 24
minutes = all_minutes % 60
print("Real time - ", hours, ":", minutes)
