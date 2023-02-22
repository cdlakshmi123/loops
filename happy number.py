# n= int(input("enter the number"))
# i=n
# while i>=10:
#     sum=0
#     while i>0:
#         j=i%10
#         sum=sum+j**2
#         i=i//10
#     i=sum
# if i==1:
#     print("n,is happy number")
# else:
#     print("no")
# n=int(input("enter the rows:"))
# i=0
# while i<n:
#     k=0
#     while k<n-i-1:
#         print("",end=" ")
#         k=k+1
#     j=0
#     while j<=i:
#        print("*",end=" ")
#     j=j+1
# i=i+1
# print()   

i=1
sum=0
while i<=100:
    s=sum+i
    i=i+1
    print(s)