X = []
Y = []
k = 0
for i in range(8):
    X.append(int(input("Enter X: ")))
    Y.append(int(input("Enter Y: ")))
for x in range(8):
    if X.count(x) > 1:
        k += 1
    for y in range(x + 1, len(Y)):
        if abs(X[x] - X[y]) == abs(Y[x] - Y[y]):
            k += 1
        if Y.count(y) > 1:
            k += 1
if k > 0:
    print("YES")
else:
    print("NO")
