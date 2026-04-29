num=int(input("enter the value"))
temp=num
sum=0
while num>0:
    last=num%10
    sum=sum+last**3
    num=num//10
if temp==sum:
    print("it is armstrong") 
else:
    print("it is not armstrong")       