#reversal of input without inbuilt commands
num=int(input("enter"))#12345
total=0 #54321
while num>0: #0>0#False
  last=num%10 #1
  total=total*10+last
  num=num//10
print(total)
