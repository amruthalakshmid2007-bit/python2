num=int(input("enter the number"))

#print welcome when num only divisible by 5and 3
if num%3==0 and num%5:
  print("welcome")
  #print hi when num only divisible by 3
elif num%3==0:
   print("hi")
 
#print hello when num only divisible by 5
elif num%5==0:
  print("hello")
 
#quit neither of the above cases
else:
  print("quit")