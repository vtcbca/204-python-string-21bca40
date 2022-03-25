a=int(input("Enter any number:"))
sum=0
no=a
while(a!=0):
    sum=sum+a%10
    a=a//10
    print("Sum of digit of{} is sum {}".format(a,sum))
    
