n=int(input("enter the number"))
a=len(str(n))
i=n
sum=0
while n>0:
    j=n%10
    b=j**a
    sum=sum+b
    n=n//10
if sum==i:
    print("armstrong")
else:
    print("not a armstrong number")



# a=int(input("no of girls:"))
# b=int(input("no of beds:"))
# if a>b:
#     print(a-b,"beds is more" )
# elif a==b:
#     print("unecessary")
# else:
#     print("no")        