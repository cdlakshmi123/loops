n=int(input("enter the number:"))
i=n
sum=0
while i>0:
    j=i%10
    sum=sum+j
    i=i//10
if n%sum==0:
    print("harshad number")
else:
    print("no")