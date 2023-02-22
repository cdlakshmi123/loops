# a=4
# b=5
# print(a+b)


# user=int(input("enter the number"))
# i=1
# while i<=4:
#     if user %2==0:
#         print(user)
#     else:
#         print(user/2)
#     i=i+1

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    if b>c:
        print("b,is median")
    else:
        print("c,is median") 
elif b>c and b>a:
    if c>a:
        print("c,is median")
    else:
        print("a,is median")
elif c>a and c>b:
    if a>b:
        print("a, is median")
    else:
        print("b,is median")     
else:
    print("no")
  