List = input("List: ").split()
n = 0
for i in List:
    n += ((List.count(i) * (List.count(i)-1)) / 2) / List.count(i)
print("couples:", int(n))
