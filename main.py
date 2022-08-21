from tkinter import *
import datetime
root = Tk()
root.geometry("600x400")
Label(root,text="Welcome to Codetutor" ,font= "Arial 22", justify=CENTER).pack()
root.title("Codetutor")
def submit():
    n = Nameval.get()
    a = ageval.get()
    e = emailval.get()
    v = vil.get()

    f = open("order.txt","a")
    f.write("\n")
    f.write(f"Name:{n}")
    f.write("\n")
    f.write(f"Age:{a}")
    f.write("\n")
    f.write(f"Email:{e}")
    f.write("\n")
    f.write(f"Value:{v}")
    f.write("\n")
    f.write(f"Date & Time:{datetime.datetime.strftime('%H:%M:%S')}")
    f.write("\n")

    

Name = Label(root,text="Name:",font="Arial 11").place(x=200,y=50)
Nameval = StringVar()
nameentry = Entry(root, textvariable=Nameval).place(x=250,y=50)

age = Label(root,text="Age:",font="Arial 11").place(x=200,y=75)
ageval = StringVar()
ageentry = Entry(root, textvariable=ageval).place(x=250,y=75)

email = Label(root,text="Email:",font="Arial 11").place(x=200,y=100)
emailval = StringVar()
emailentry = Entry(root, textvariable=emailval).place(x=250,y=100)

Label(root,text="Language that you want to learn:").place(x=250,y=125)
vil = IntVar()
Radiobutton(root, text="Python",padx = 20, variable=vil, value=1).place(x=250,y=150)

Radiobutton(root,text="C++",padx = 20, variable=vil,value=2).place(x=250,y=175)
Radiobutton(root,text="HTML,CSS,JS",padx = 20, variable=vil,value=3).place(x=250,y=200)
Radiobutton(root,text="Flask",padx = 20, variable=vil,value=4).place(x=250,y=225)
Radiobutton(root,text="Java",padx = 20, variable=vil,value=5).place(x=250,y=250)
Radiobutton(root,text="Django",padx = 20, variable=vil,value=6).place(x=250,y=275)

Button(text="Submit",pady="5",borderwidth=2,justify=CENTER,command=submit).place(x=300,y=310)






root.mainloop()