#reversal of input without inbuilt commands
num=int(input("enter"))#12345
original=num
total=0 #54321
while num>0: #0>0#False
  last=num%10 #1
  total=total*10+last
  num=num//10
print(total)  
#to check whether it is palindrome or not
if original==total:
  print("it is palindrome")
else:
   print("it is not palindrome")
 
