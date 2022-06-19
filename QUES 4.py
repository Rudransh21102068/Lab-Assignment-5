n=int(input("Enter the no. of rows :"))
t=(n//2)+1
l=n//2
for i in range(1,t+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for q in range(l,0,-1):
    for r in range(q,0,-1):
        print("*",end="")
    print()
