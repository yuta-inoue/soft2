dict = {}

def sort(dic):
    return sorted(dic.items())

def disp_name(name):
    print(name,dict[name])

def disp_age(age):
    for k in dict:
        if dict[k] == age:
            print(k,dict[k])

def add(name,age):
    dict[name] = age

def delete(name):
    del dict[name]

print("append")
add("john",10)
add("tarou",20)
add("itirou",30)
add("yamada",40)
print(dict)

print("sort")
print(dict)
print(sort(dict))

print("delete")
delete("john")
print(dict)
