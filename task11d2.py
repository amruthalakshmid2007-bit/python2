num=int(input("enter the number"))
if num==0:
 print("factorial=1")
i=1
fact=1
while i<=num:
 fact=fact*i
 i+=1
print(f"{fact}") 