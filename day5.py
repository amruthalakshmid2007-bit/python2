# import math
# print(math.sqrt(5))
# import math
# print(math.pow(5,2))

#----creating my own module----#
# import arith
# print(arith.sqrt(5,2))
#-----creating an object-----#
# a=5
# print(type(a))
# class Building:#(class is the keyword used to design the object)
#     #def staircase()
#     pass
# # leaving an empty block of code by using the
# building1=Building()#(like calling the builder to execute the designed plan)
# print(type(building1))


# class student():
#     pass
# st1=student()

# class Computer:
#     def powerOn(self):
#         print("Computer Switched On....")
 
 
# com1=Computer()
# # Computer.powerOn(com1) calling an object
# com1.powerOn() #(to switch on the specific computer) or calling the object specifically     


# class ComputerShop:
#     def __init__(self,r,h):
#        self.ram=r
#        self.hdd=h

#     def powerOn(self):
#       print("Computer Switched On...")

#     def config(self):
#         print(f"{self.ram} of Ram and {self.hdd} of HDD")    

# # com1=ComputerShop()
# # com1.config()
  
# com1=ComputerShop("8 GB","500 GB ")
 
# com1.config()
# # com1.config()
# com2=ComputerShop("32 GB","1 TB ")
# com2.config()



# file=open("demo.txt","w")#writing=w
# file=open("demo.txt","w")
# file.write("this is my new line") output:this is my new linethis is my new line2
# file.write("this is my new line2")
# file.close()
# file=open("demo.txt","a")#adding
# file.write("this is my new line")#output:this is my new linethis is my new line2this is my new line
# file.close()

# file=open("demo.txt","a")#adding
# file.write("\nthis is my new line")#output:this is my new linethis is my new line2this is my new line
#                                            #   this is my new line
#                                            #op added to the past outputs of the similer problem
# file.close()



# file=open("demo.txt",'r')#reading
# contents=file.read()
# print(contents)
# file.close()

# file=open("demo.txt",'r')
# print(file.tell())#0
# contents=file.read(6)
# print(file.tell())#6
# file.seek(0)
# print(file.tell())#0
# print(contents)
 
# file.close()    
# words=[]
# with open("demo.txt",'r') as f:
    
#     # print(f.readline())#read line by line and executes line by line
#     for line in f.readlines():
#      for word in line.split():
#         words.append(word)
# print(words)



# with open("StockCake-Evening_park_lights-1261677-medium.jpg","rb") as file:
#     content=file.read(500)
#     with open("demo1.jpg","wb") as file:
#       file.write(content)

#to remove File
# import os
#os.remove("test.txt")
#os.mkdir("testFolder")
# open(r"testFolder\demo.txt","x")
#file=open("test.txt","x")
#file.close()
# print(os.path.exists(r"testFolder\demo1.txt"))


with open("demo.txt") as file:
    #  lst=file.readlines()
#     print(len(lst))
   print(len(file.read().split()))


