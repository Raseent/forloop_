num=int(input("enter a number:"))
print(num)

num2=int(input("enter another number:"))
print(num2)
print("Those are the operators tou can use:")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Divition")
print("5 modulus")
sum=input("Please choose an operation from these(1,2,3,4,5):")

if sum=="1":
    print("the sum of two number:",num+num2)

    print("Addition")
if sum=="2":
    print("the sum of two number:",num-num2)
    print("2.Substraction")
if sum=="3":
    print("the sum of two number:",num*num2)
    print("3.Multiplicatio")
if sum=="4":
    print("the sum of two number:",num/num2)
    print("4.Divition")
if sum=="5":
    print("the sum of two number:",num%num2)
    print("5.modulus")








