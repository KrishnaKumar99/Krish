n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    pal=n%10
    rev=rev*10+pal
    n=n//10
if(temp==rev):
    print("yes")
else:
    print("no")
