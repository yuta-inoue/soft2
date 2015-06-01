def zip(x,y):
    arr = []
    for i in range(len(x)):
        arr.append([x[i],y[i]])
    return arr

z = zip([1,2,3,4],['a','b','c','d'])
print(z)
