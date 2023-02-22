# i=0
# min=500
# max=0
# while i<=n:
#     n=int(input("enter the number"))
#     if n>max:
#         max=n
#     elif n<min:
#         min=n
#     i=i+1
# print("largest number is",max)
# print("smallest number is",min)


# r=4
# c=4
# i=0
# while i<=r:
#     j=0
#     while j<=c:
#         if (i==2 and j!=1 and j!=2 and j!=3)or (i==1 and j!=0 and j!=2 and j!=4)or (i==0 and j!=0 and j!=1 and j!=3 and j!=4)or (i==3 and j!=0 and j!=2 and j!=4) or (i==4 and j!=0 and j!=1 and j!=3 and j!=4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()

# r=3
# c=6
# i=0
# while i<=r:
#     j=0
#     while j<=c:
#         if (i==3)or (i==2 and j==1)or (i==2 and j==5)or (i==1 and j==2)or (i==1 and j==4)or (i==0 and j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()



# a=input("enter the name:")
# if a==a:
#     print("exam=1.maths exam  2.english 3.algebra  4.cultur fit")
#     exam=int(input("enter test"))
#     result=input("enter result:")
#     if exam==1:
#         if result=="pass":
#             print("go to second exam")
#         else:
#             print("betterluck next time")
#     elif exam==2:
#         if result=="pass":
#             print("go to third exam")
#         else:
#             print("practies more")
#     elif exam==3:
#         if result=="pass":
#             print("go to fourth exam")
#         else:
#             print("practies maths questions")
#     elif exam==4:
#         if result=="pass":
#             print("take your admission letter")
#         else:
#             print("prepare for fourth round")
#     else:
#         print("enter valid data")
# else:
#     print("invalid data")


# a=int(input("enter the num"))
# b=int(input("enter the num"))
# c=int(input("enter the num"))
# if a>=100 and a<=999:
#     print("+","(",a,")",end="")
#     if b>=100 and b<=999:
#         print(b,end="")
#         if c>=1000 and c<=9999:
#             print("-",c,end="")
#         else:
#             print("no")
#     else:
#         print("no")
# else:
#     print("no")


i=1
counter=891
while i<=40:
    if i%3==0:
        counter==i-891
        print(i)
    i=i+1
