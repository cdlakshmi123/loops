n=int(input("enter the number"))
num=n
i=0
while n>0:
    a=n%10
    i=i*10+a
    n=n//10
if i==num:
    print("palindrome")
else:
    print("not a palindrome")