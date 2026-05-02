class Student:
    def __init__(self,name,usn,s1,s2,s3):
        self.name=name
        self.usn=usn
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def avg(self):
        print((self.s1+self.s2+self.s3)/3)
        
stud1=Student("Arya",12,98,99,97)
stud2=Student("Raavya",42,89,97,98)    
stud1.avg()  
stud2.avg()  
