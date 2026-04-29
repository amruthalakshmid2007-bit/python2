
#take the input of 3 numbers
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
#check whether number1 is greatest
if num1>num2&num1>num3:
   print("number1 is greatest")
    #check whether number2 is greatest 
elif num2>num3&num2>num1:
    print("number2 is greatest")
    #check whether number3 is greatest
else:
    print(":number3 is the greatest")