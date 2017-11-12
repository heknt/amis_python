k1 = int(input("First group: "))
k2 = int(input("Second group: "))
k3 = int(input("Third group: "))
tab1 = (k1 // 2)+(k1 % 2)
tab2 = (k2 // 2)+(k2 % 2)
tab3 = (k3 // 2)+(k3 % 2)
tab = tab1+tab2+tab3
print("Number of tables:", tab)
