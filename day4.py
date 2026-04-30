# def greet():
#     print("Hello user")
#     print("Hello user")
#     print("Hello user")
#     print("Hello user")
# greet()    

# def add(a,b):
#     print(a+b)
# m=30
# n=65
# add(m,n)  
# ---------positional arguments----#  

# def add(a,b,c):
#     print(f"a is{a} and b is{b} and c is{c}")
# add(5,6,7)   
 
#-------variable Arguments-----#
# def add(*b):
#      print(b)
# add(5,6,7) 
  
#------keyword arguments-----#

# def login (password,uname):
#     print(f"Name is:{uname}|nPassword is :{password}")
# login(uname="Logu",password="123")

#Keyword variable length arguments
# def register(age=18,**b):
#      print(b)
# register(uname=shridevi,age,)     
# def register(age=18):
#           print(age)
# register()   


a=5
def hi():
    a=10
    print(a)
    globals()['a']=15
hi()    
print(a)