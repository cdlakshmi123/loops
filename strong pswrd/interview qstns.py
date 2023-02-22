# a=int(input("num"))
# b=int(input("num"))
# c=int(input("num"))
# if a>b and a<c:
#     print("a is sec max") 
# elif b>a and b<c:
#     print("b is  sec max")
# else:
#     print("c is sec max")

# n= int(input("num"))
# i=1
# k=ord("A")
# while i<=n:
#     j=1
#     while j<=i:
#         print(chr(k),end="")
#         k=k+1
#         j=j+1
#     i=i+1
#     k=k-1
#     print()

a=[2,3,5,9]
i=0
max=0
sec=0
while i<len(a):
    b=a[i]
    if b>max:
        max=b
    elif b>sec and sec!=max:
        sec=b
    i=i+1 
print(sec)   

    

