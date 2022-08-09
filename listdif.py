listt=[1,2,3,54,5,6,7,8,9,10]
odd_list=[]
even_list=[]
for i in listt:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)
