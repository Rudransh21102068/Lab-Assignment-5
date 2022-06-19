x=int(input("Enter the minimum value :"))
y=int(input("Enter the maximum value: "))
num=int(input("Enter the number for divisibility check :"))
i=x
while i<=y:
    if i%num==0 :
        print(i)
    i+=1
