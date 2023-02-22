# n=int(input("enter the row"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print("*",end=" ")
#         else:
#             print(i,end=" ")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the row"))
# for i in range(n):
#     for j in range (i):
#         print(i,end="")
#     print()


a=int(input("enter the number:-"))
i=1
j=4
while i<=a:
    print(' '*j+i*'*'+' '*j)
    i=i+2
    j=j-1
i=7
j=1
while i>=1:
    print(' '*j+i*'*'+' '*j)
    i=i-2
    j=j+1

