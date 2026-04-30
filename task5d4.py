for num in range(10,61):
  for i in range(10,num):
    if num%i==0:
        break
  else:
    print(num)        
