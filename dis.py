dict={1:"he",2:"she",3:"that"}
print(dict[1])
print(dict[2])
print(dict[3])


print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get(1))
print(dict.get(2))
dict.update({4:"him"})
print(dict)
dict["5"]="i"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print(dict)
del dict[2]
print(dict)
dict.clear()
print(dict)
print("===============================================")
dict={1:"he",2:"she",3:"i"}
for i in dict:
print(i)



