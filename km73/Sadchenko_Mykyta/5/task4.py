n = int(input("N: "))  # кількість кеглів
N = n * "I".split()
k = int(input("K: "))  # кількість шарів
l_begin = 0
r_end = 0
for i in range(1, k+1):
    l_begin = int(input("l: "))  # початок інтервалу збитих кеглів
    r_end = int(input("r: "))  # кінець інтервалу збитих кеглів
    for j in range(n):
        if l_begin <= (j+1) <= r_end:
            N.pop(j)
            N.insert(j, ".")
print(''.join(str(h) for h in N))
