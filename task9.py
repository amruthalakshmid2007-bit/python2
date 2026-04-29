#get no. of units of electricity consumed
unit=int(input("enter the no.of units consumed"))
#cal amount of rupees paid by the user
if unit<=200:
    print("Rs 0")
elif unit <=300:
  rs1=(unit-200)*1.5
  print("amount:",rs1)
elif unit <=400:     
  unit=unit-300
  rs2=unit*3+(100*1.5)
  print("amount:",rs2) 
elif unit <=500:     
  unit=unit-400
  rs3=unit*5+(100*1.5)+(100*3)
  print("amount:",rs3) 
else:     
  unit=unit-500
  rs4=unit*7+(100*1.5)+(100*3)+(100*5)
  print("amount:",rs4)           
#slab:unit<=200 rs0/unit
#201-300  rs1.5  301-400   rs3 unit   401-500  rs5  >500 7rs
