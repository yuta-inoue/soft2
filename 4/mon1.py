def rotate(x):
    a = x[1:]
    a.append(x[0])
    return a

y = rotate([0,1,2,3])
print(y)
