lower_value = int(input("Enter the Lowest Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))    # input from user the lowest and the upper range
  
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):                           # Check for each number if it has any factor between 1 and itself
            if (number % i) == 0:                             # if YES, the code will move on
                break       
        else:  
            print (number)                                    # if NO, the code prints the number
