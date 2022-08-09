vowels_constants=['a','e','i','o','u','r','t','w','A','P','X','O','U']
vowels=['a','e','i','o','u']
vowels_list=[]
constants_list=[]
for i in vowels_constants:
    i=i.lower()
    if i in vowels:
        vowels_list.append(i)
    else:
        constants_list.append(i)
print(vowels_list)
print(constants_list)
print("===================================================")


string="luminar is the Best"
lower_count=0
upper_count=0
space_count=0
for i in string:
    if i.islower():
        lower_count+=1
    elif i.isupper():
        upper_count+=1
    else:
        i.isspace()
        space_count+=1
print("lower_count:",lower_count)
print("upper_count:",upper_count)
print("space_count:",space_count)
print(
    '====================================')


sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
