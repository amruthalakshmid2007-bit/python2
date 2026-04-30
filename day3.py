#--case conversion in strings--#
# s="I love Java"
# us=s.upper()
# print(us)
# print(s)
# ls=us.lower()
# print(ls)
# ts=s.title()
# print(ts)
# cs=ls.capitalize()
# print(cs)

# s="python programming"
# print(s.find("an")) if not present gives -1 as output
# print(s.index("thon"))#2 as output because 1st letter's index is printed
# print(s.index('o')) 4


# s="python programming"
# print(s.find("p"))
# print(s.index("thon"))
# print(s.index('on'))
# print(s.startswith("pi"))
# print(s.endswith("ing"))

# s="I like Java"
# rs=s.replace("Java","Python")
# print(rs)

# s="I like Java"
# sl=s.split()
# print(sl)

# lst=input("enter a list of numbers")
# print(lst.split(","))

# s=["Hi","all","good","morning","to","everyone"]
# ls=' '
# ls1=ls.join(s)
# print(ls1)

# s=" Shridevi"
# s1=s.lstrip()#removes the spaces if l--left,r--right
# print(s)
# print(s1)

# s="Shridevi"
# print(len(s))
# print(s.count("i"))
# print(s.isdigit())
# print(s.isalpha())
# print(s.isalnum())

# name=input("enter:")#logu
# count=0 #5
# while count<5:
#     print(name)#logu logu logu logu logu
#     count+=1
 
# start=1
# while start<=100:
#     print(start)
#     start+=1


#num1=int(input("enter:"))
# num2=int(input("enter:"))

# while num1<=num2:
#     if num1%2==0:
#         print(num1)
#     num1+=1   

# num=int(input("enter"))
# fact=1
# for ele in range(1,num+1):
#     fact*=ele
# print(fact)    


num=int(input("enter:"))
first=0
second=1
while first<=num:
    print(first)
    third=first+second
    first,second=second,third
