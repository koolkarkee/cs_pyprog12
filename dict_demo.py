d1 = dict()
d1["key"] = "value"
print(d1)

d1 = {
    "name" : "bibek", 
    "age" : 33
}

print(d1)

d2 : dict = {}
d3 = {}
print(type(d2))
print(type(d3))
print(d1.keys(), end = "|")
print(type(d1.keys())) 

for keys in d1.keys():
    val = d1[keys]
    print(keys, " is ", val)

