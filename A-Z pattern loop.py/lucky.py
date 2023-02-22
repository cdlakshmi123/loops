# n=int(input ("enter the row"))
# i=1
# k=ord("A")
# while i<=n:
#     j=1
#     while j<=i:
#         if i%2!=0:
#             print(i,end="")
#         else:
#             print(chr(k),end="")
#         j=j+1
#     i=i+1
#     k=k+1
# 
# 
# 
# 
# n=input("enter the user")
# a=len(n)
# i=0
# while i<=a:
#     k=0
#     while k<=a-i:
#         print(" ",end=" ")
#         k=k+1
#     j=i
#     while j>=0:
#         print(n[j],end=" ")
#         j=j-1
#     i=i+1
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#        print(i,end="")
#        j=j+1
#     i=i+1
#     print()

n=int(input("enter the row"))
i=1
k=ord("s")
while i<=n:
    l=0
    while l<=n-i:
        print(" ",end=" ")
        l=l+1
    j=1
    while j<=i:
        if i%2==0:
            print(chr(k),end=" ")
        else:
            print(i,end=" ")
        j=j+1
    print()
    i=i+1
    k=k+1