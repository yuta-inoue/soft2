def mean(x):
    tot = 0
    for dx in x:
        tot+=dx
    return 1.0*tot/len(x)
def variance(x):
    tot = 0
    m = mean(x)
    for dx in x:
        tot += (dx-m)**2
    return 1.0*tot/len(x)


x = [1,2,3,4,5,6,7,8,9,10]

print(mean(x))
print(variance(x))
