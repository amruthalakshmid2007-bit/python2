#------list------#

# first=[1,2,3,4,5]
# print(type(first))
# print(first[0])
# first.append(4)#1,2,3,4,5,4
# print(first)
# first.insert(2,6)#1,2,6,3,4,5,4
# print(first)
# first.extend([7,8,9])#1,2,6,3,4,5,4,7,8,9
# print(first)
# print(first.count(4))#2
# print(first.index(5))#5
# first.remove(9)#1,2,6,3,4,5,4,7,8
# print(first)
# first.pop()#1,2,6,3,4,5,4,7
# print(first)
# first.pop(3)#1,2,6,4,5,4,7
# print(first)
# first.remove(4)#1,2,6,5,4,7
# first.clear()#[]
# del first
# print(first)#error
# first=[45,78,25,36,96,45,83,53]
# first.sort()
# first.reverse()
# print(len(first))
# max(first)
# sum(first)
# first[6].count(30)
# lst=[1,2,3,4,5]
# nlst=lst.copy()
# nlst[0]=6
# print(lst)
# print(nlst)
#----------tuple------------#

#tpl=(1,2,3,4,5)
# print(type(tpl))
# t=1,2,3
# print(type(t))
# t=(6,)#immutable
# print(type(t))
# tpl[0]=6
# print(tpl.count(5))
# print(tpl.index(5))
# stpl=sorted(tpl,reverse=True)
# print(stpl)
#---------sets---------#

# s={25,42,85,35,12,45,96,85,32,45,78,65,96,32,54,45}
# print(s)

# s={}
# print(type(s))#class dictionery
# s=set()
# print(type(s))
# s.add(5)#unordered so we cannot use appendhence add
# s.update([6,7,8,9,10,11,12])
# print(s)
# s.remove(5)
# print(s)
# #s.remove(13) error
# s.discard(13)#it removes the value if it is present else will not do anything
# #removing a random value
# s.pop()
# print(s)
# s.clear()
# print(s)

#-------union-----#
#a={1,2}
#b={3,4,5}
# a=a.union(b)#combines both a and b and stores in a
# print(a)
# b.add(6)
# print(b)
# print(a.intersection(b))
# print(a.difference(b))
# # print(a.symmetric_difference(b))
# a={1,2}
# b={1,2,3,4,5}
# print(a.issubset(b))#true
# print(b.issuperset(a))#true
# print(a.isdisjoint(b))#false

#----------dictionery--#
# d={"a":1}
# d["b"]=2
# print(d)
# d["a"]=3
# print(d)
# d[4]=5
# print(d)
# d[(1,2)]
# print(d)
# d[(1,[2])]
# print(d)
 
# d[(1,[2])]="str"
# d={1:"sunday",2:"monday",3:"tuesday"} op with3
# print(d[1])                           
# d.pop(2)
# print(d)
# d.popitem()
# print(d)
# #d.clear()
# #print(d)
# print(d.keys())
# print(d.values())
 #----while loop---#
#initialization
i=0
#where to end-->condition
while i<5:
    #what to do--->statements
    print("shridevi")
    #how to move-->incre/decrement
    i+1