# n=int(input("enter the num"))
# i=0
# while i<=n:
#     j=i
#     while j>=0:
#         print(j,end=" ")
#         j=j-1
#     i=i+1
#     print()

# i=5
# while i>=1:
#     j=1
#     while j<=5:
#         print(j,end="")
#         j=j+1
#     i=i+1
#     print()



# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print(j+1,end=" ")
#         j=j+1
#     i=i+1
    # print()


# n=int(input("enter the row"))
# i=0
# while i<n:
#     j=n
#     while j>i:
#         print(j,end="")
#         j=j-1
#     i=i+1
#     print()

# n=int(input("enter the row"))
# i=n
# while i>=1:
#     j=n
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     i=i-1
#     print()

r=4
c=8
i=0
while i<=r:
    j=0
    while j<=c:
        if i==5 or (i==3 and j!=8 and j!=6 and j!=4 and j!=2 and j!=0)or (i==2 and j!=8 and j!=7 and j!=5 and j!=3 and j!=1 and j!=0) or (i==2 and j!=8 and j!=7 and j!=5 and j!=3 and j!=1 and j!=0) or (i==1 and j!=8 and j!=7 and j!=6 and j!=4 and j!=2 and j!=1 and j!=0) or (i==0 and j!=8 and j!=7 and j!=6 and j!=5 and j!=3 and j!=2 and j!=1 and j!=0) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()

# n=int(input("enter the row"))
# i=1
# k=1
# while i<=n:
#     j=0
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#         k=k+1
#     i=i+1
#     print()

# n=int(input("enter the row"))
# i=1
# while i<=n:
#     k=0
#     while k<=n-i:
#         print("  ",end="")
#         k=k+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     i=i+2
#     print()

# year=int(input("enter the year"))
# month=int(input("enter the month"))
# date=int(input("enter the date"))
# if month==4 or month==6 or month==9 or month==11:
#     if date<30:
#         print(date+1,"-",month,"-",year)
#     else:
#         print("1","-",month+1,"-",year)
# elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
#     if date<31:
#         print(date+1,"-",month,"-",year)
#     else:
#         print("1","-",month+1,"-",year)
# elif month==12:
#     if date<31:
#         print(date+1,"-",month,"-",year)
#     else:
#         print("1","-","1","-",year+1)
# elif year%4!=0:
#     if month==2:
#         if date<28:
#             print(date+1,"-",month,"-",year)
#         else:
#             print("1","-",month+1,"-",year)
#     else:
#         print("invalid data")
# elif year%4==0:
#     if month==2:
#         if date<29:
#             print(date+1,"-",month,"-",year)
#         else:
#             print("1","-",month+1,"-",year)
#     else:
#         print("enter valid number")
# else:
#     print("enter valid data")


# n=int(input("enter the row"))
# i=1
# v=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(v,end=" ")
#         j=j+1
#         v=v+2
#     i=i+2
#     print()

# a="python solving and python programming"
# print("'",a[0:6],"'",",","'",a[6:13],"'",",","'",a[13:16],"'",",","'",a[16:22],"'",",","'",a[22:26],"'",",","'",a[26:33],"'")




# a="python solving and python programming"
# print(a.split())

# n=int(input("enter the row"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("#",end=" ")
#         j=j+1
#     i=i+1
#     print()    




# n=int(input("enter the row"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     i=i+1
#     print()

# n=int(input("enter the num"))
# if n<=100:
#     print("no charge")
# elif n>=101 and n<=199:
#     v=n-100
#     print(v*5)
# elif n>200:
#     v=n-200
#     print(v*10)

