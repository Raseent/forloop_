newlist=[1,2,3,4,5,6]
print(newlist)
newlist.clear()
print(newlist)




thislist=["bubble","bugati","anar","ujala","aa","aurain"]
print(thislist)
print(thislist.sort())
print(thislist.sort(reverse=True))
thislist.sort(reverse=True)
print(thislist)


thislist.sort()
print("========================================================")
this=["bubble","bugati","anar","ujala","aa","aurain"]
this.sort(reverse=True)
print(thislist)
print("========================================================")
list1=['a','b','c']
list2=['e','f','g']
list3=['h','i','j']
list4=list1
list4.append('100')
print(list1)
list5=list1.copy()
list5.append('200')
print(list5)
print(list1)
print("===============================================================")



tuplee=(1,2,3,4,)
print(tuplee)
print(len(tuplee))
print(tuplee[0:2])
print(tuplee[0:1])
print(tuplee[0:3])
print(tuplee.count(5))
print(tuplee.index(1))
print("==============================================================")
fruits=("apple","banana","chery","guava","mango","pineapple")
*a,b,c,d=fruits
print(a)
print(b)
print(c)
print(d)


print("================================================================")

ttuple=(1,2,3,4)

ttuple=list(ttuple)
ttuple.append(5)
ttuple=tuple(ttuple)
print(ttuple)
print("==========================================================")
set={1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5}
print(set)
print("==========================================================")
set.remove(1)
print(set)
print("====================================================")
set.discard(2)
print(set)
print("======================================================")
set.pop()
print(set)
print("===================================================")
set.clear()
