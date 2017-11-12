coord = input("Enter x1 y1 x2 y2:").split()


def distance(x1, y1, x2, y2):
    result = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(result, 3)


print(distance(float(coord[0]), float(coord[1]), float(coord[2]), float(coord[3])))
