"""WAS to print this pattern
        *
       **
      *** """ 

n=int(input("Enter No. of rows : "))
for i in range (n):
    for j in range (l,n-i):
        print(end=" ")
    for j in range (i+1):
        print("* ",end="")
    print()
        
