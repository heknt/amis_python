List = input("List: ").split()
newList = []
for i in List:
    if List.count(i) == 1:
        newList.append(i)
for elem in newList:
    print(elem, end=" ")
