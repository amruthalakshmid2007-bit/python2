from tkinter import *
window=Tk()
window.geometry("450x550+100+50")
window.config(background="#FFFFFF")
res=StringVar()
exp=StringVar()
res.set("0.00")
def click(n):
    if n=="+" or n=="-" or n=="/" or n=="*":
        pass
    elif n=="=":
        pass
    else:
        exp.set(exp.get()+n)
        print(exp.get())

Label(textvariable=res,height=6,width=20,bg="#3A3B3B00").grid(row=1,column=0,columnspan=4)

btn1=Button(text="9",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn2=Button(text="8",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn3=Button(text="7",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn4=Button(text="6",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn5=Button(text="5",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn6=Button(text="4",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn7=Button(text="3",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn8=Button(text="2",width=7,height=3,bg="#17A2BA",fg="#0F0E0E",font=("Arial",16,"bold"))
btn9=Button(text="1",width=7,height=3,bg="#17A2BA",fg="#0F0E0E" ,font=("Arial",16,"bold"))
btn10=Button(text="0",width=7,height=3,bg="#17A2BA",fg="#0F0E0E", font=("Arial",16,"bold"))
btn11=Button(text="+",width=7,height=3,bg="#B470A8",fg="#0F0E0E" ,font=("Arial",16,"bold"))
btn12=Button(text="-",width=7,height=3,bg="#B470A8",fg="#0F0E0E" ,font=("Arial",16,"bold"))
btn13=Button(text="*",width=7,height=3,bg= "#B470A8",fg="#0F0E0E" ,font=("Arial",16,"bold"))
btn14=Button(text="/",width=7,height=3,bg= "#B470A8" ,fg="#0F0E0E" ,font=("Arial",16,"bold"))
btn15=Button(text="=",width=7,height=3,bg= "#B470A8" ,fg="#0F0E0E" ,font=("Arial",16,"bold"))
btn16=Button(text=".",width=7,height=3,bg= "#B470A8" ,fg="#0F0E0E" ,font=("Arial",16,"bold"))

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=1,column=4)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=2,column=3)
btn8.grid(row=2,column=4)
btn9.grid(row=3,column=1)
btn10.grid(row=3,column=2)
btn11.grid(row=3,column=3)
btn12.grid(row=3,column=4)
btn13.grid(row=4,column=1)
btn14.grid(row=4,column=2)
btn15.grid(row=4,column=2)
btn16.grid(row=4,column=2)



window.mainloop()