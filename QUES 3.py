a=float(input("Enter the length of side:"))
b=float(input("Enter the length of side:"))
c=float(input("Enter the length of side:"))
if a+b>c and a+c>b and b+c>a :
    s=(a+b+c)/2
    ar_tri=(s*(s-a)*(s-b)*(s-c))**(0.5)
    print(ar_tri)
else :
    print("Error")
