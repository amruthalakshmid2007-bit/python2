name=input("Enter your name:")#Rajesh
print(f"welcome,{name},and How are you?")
# "Welcome Rajesh and How are you?"
#1. get marks from student
mark=int(input("Enter your mark:"))
#2.check mark is greater than 35
if mark>=35:
#3. print pass
   print("pass")
   #check mark greater than 90
   if mark>=90:
      #printmedical
      print("medical")
      #check mark>=75
   elif mark>=75:
      #print engineering  
      print("engineering")
   else:
      #print degree
      print("degree")  
else:   
#4. print fail
   print("fail")