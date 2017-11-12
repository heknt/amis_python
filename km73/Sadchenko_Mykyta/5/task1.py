row = input("height of each: ").split()
petya = input("height of Petya: ")
row.sort()
row.reverse()
List = []
for i in range(len(row) - 1):
    if (petya <= row[i-1]) and (petya > row[i]):
        List.append(petya)
    List.append(i)
print("Petya is on the line:", List.index(petya) + 1)
