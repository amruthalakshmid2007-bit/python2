num=int(input("enter the number"))
rev=0
while num>0:
  last=num%10
  num=num//10
  rev=rev*10+last

print(rev)
  #check whether the given number is a polynomial or not