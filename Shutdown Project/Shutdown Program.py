from tkinter import *
from tkinter import messagebox as box
from os import *
from PIL import Image,ImageTk 
root=Tk()
root.geometry("850x700")
imag1e=PhotoImage(file="c:\\Users\\haris\\Desktop\\New folder\\switch.png")
root.iconphoto(False,imag1e)
root.config(bg="crimson")
root.title("Shutdown Options")

def shut_min():   
    root=Tk()
    root.geometry("1050x450")
    root.config(bg="#202020")
    root.title("Minutes")

    def count1():
        p=v21.get()
        o=int(p*60)
        b=int(o/60)
        system(f"shutdown /s /t {o}")
        v=box.askquestion("Info",f"Shutdown is shedule after {b} minutes \n Do you want to abort (click yes) ")
        if v=="yes":
            system("shutdown /a")
        else:
            exit()
    v=Frame(root,padx=200,pady=100,bg="grey")
    v.pack(pady=50)
    v1=Label(v,text="Enter Minutes",font="cosmic 20 bold",bg="grey",fg="black")
    v1.grid()
    v21=IntVar(root)
    root.setvar(value=v21)
    v3=Entry(v,textvariable=v21)
    v3.grid(row=0,column=1,padx=10)
    btn=Button(v,text="Submit",font="cosmic 10 italic",padx=40,pady=5,command=count1)
    btn.grid(row=1,column=1,pady=20)
    root.mainloop()
    
def shut_hour():
    root=Tk()
    root.geometry("1050x450")
    root.config(bg="#202020")
    root.title("Hours")

    def count():
        p=v2.get()
        o=int(p*3600)
        b=int(o/60)
        system(f"shutdown /s /t {o}")
        v=box.askquestion("Info",f"Shutdown is shedule after {v2.get()} hours \n\n Do you want to abort (click yes)")
        if v=="yes":
            system("shutdown /a")
        else:
            exit()
    v=Frame(root,padx=200,pady=100,bg="grey")
    v.pack(pady=50)
    v1=Label(v,text="Enter Hours",font="cosmic 20 bold",bg="grey",fg="black")
    v1.grid()
    v2=IntVar(root)
    root.setvar(value=v2)
    v3=Entry(v,textvariable=v2)
    v3.grid(row=0,column=1,padx=10)
    btn=Button(v,text="Submit",font="cosmic 10 italic",padx=40,pady=5,command=count)
    btn.grid(row=1,column=1,padx=20,pady=20,)
    root.mainloop()

def res_min():   
    root=Tk()
    root.title("Minutes")

    root.geometry("1050x450")
    root.config(bg="#202020")
    def count1():
        p=v21.get()
        o=int(p*60)
        b=int(o/60)
        system(f"shutdown /s /t {o}")
        v=box.askquestion("Info",f"Shutdown is shedule after {b} minutes \n\n Do you want to abort (click yes)")
        if v=="yes":
            system("shutdown /a")
        else:
            exit()
    v=Frame(root,padx=200,pady=100,bg="grey")
    v.pack(pady=50)
    v1=Label(v,text="Enter Minutes",font="cosmic 20 bold",bg="grey",fg="black")
    v1.grid()
    v21=IntVar(root)
    root.setvar(value=v21)
    v3=Entry(v,textvariable=v21)
    v3.grid(row=0,column=1,padx=10)
    btn=Button(v,text="Submit",font="cosmic 10 italic",padx=40,pady=5,command=count1)
    btn.grid(row=1,column=1)
    root.mainloop()

def res_hour():   
    root=Tk()
    root.title("Hours")

    root.geometry("1050x450")
    root.config(bg="#202020")   
    def count1():
            p=v21.get()
            o=int(p*60)
            b=int(o/60)
            system(f"shutdown /s /t {o}")
            v=box.askquestion("Info",f"Shutdown is shedule after {b} minutes \n\n Do you want to abort (click yes)")
            if v=="yes":
                system("shutdown /a")
            else:
                exit() 
    v=Frame(root,padx=200,pady=100,bg="grey").pack(pady=50)
    v1=Label(v,text="Enter Hours",font="cosmic 20 bold",bg="grey",fg="black")
    v1.grid()
    v21=IntVar(root)
    root.setvar(value=v21)
    v3=Entry(v,textvariable=v21)
    v3.grid(row=0,column=1,padx=10)
    btn=Button(v,text="Submit",font="cosmic 10 italic",padx=40,pady=5,command=count1)
    btn.grid(row=1,column=1,padx=20,pady=20,)
    root.mainloop()

def shut_down():
    root=Tk()
    root.config(bg="#CF5430")
    root.geometry("950x550")
    root.title("Options tab")
    n=Frame(root,bg="wheat",padx=100,pady=100)
    n.pack(pady=60)
    n1=Label(n,text="Choose an option" ,font="cosmic 20 bold",bg="wheat",fg="black")
    n1.pack()
    btn=Button(n,text="Hours",font="cosmic 15 italic",padx=40,pady=5,command=shut_hour)
    btn.pack(pady=20)
    btn1=Button(n,text="Minutes",font="cosmic 15 italic",padx=30,pady=5,command=shut_min)
    btn1.pack(pady=20)
    root.mainloop()

def re_start():
    root=Tk()
    root.config(bg="#CF5430")
    root.geometry("950x550")
    root.title("Options tab")

    n=Frame(root,bg="wheat",padx=100,pady=100)
    n.pack(pady=60)
    n1=Label(n,text="Choose an option" ,font="cosmic 20 bold",bg="wheat",fg="black")
    n1.pack()
    btn=Button(n,text="Hours",font="cosmic 15 italic",padx=40,pady=5,command=res_hour)
    btn.pack(pady=20)
    btn1=Button(n,text="Minutes",font="cosmic 15 italic",padx=30,pady=5,command=res_min)
    btn1.pack(pady=20)
    root.mainloop()
    
def all_option():
    root=Tk()
    root.config(bg="#C3813C")
    root.geometry("1050x750")
    root.title("Other Options")

    al=Frame(root,padx=200,pady=50,bg="wheat")
    al.pack(pady=100)
    al_label=Label(al,text="All options",font="cosmic 20 italic",bg="wheat");al_label.pack()
    def shutdown():
        system("shutdown /s")
    def restart():
        system("shutdown /r")
    def abort():
            system("shutdown /a")
    def hibernate():
            system("shutdown /h")
    btn1=Button(al,text="Shutdown",font="cosmic 15 italic",padx=41,pady=15,command=shutdown);btn1.pack(pady=20)
    btn2=Button(al,text="Restart",font="cosmic 15 italic",padx=50,pady=15,command=restart);btn2.pack(pady=10)
    btn3=Button(al,text="Abort",font="cosmic 15 italic",padx=59,pady=15,command=abort);btn3.pack(pady=10)
    btn4=Button(al,text="Hibernate",font="cosmic 15 italic",padx=40,pady=15,command=hibernate);btn4.pack(pady=10)
    root.mainloop()
    
def Extra_Info():
    root=Tk()
    root.geometry("750x650")
    root.title("Help")

    p1=Label(root,text="Help",font="cosmic 30 bold",bg="black",fg="white",pady=10)
    p1.pack(fill=X)
    p2=Frame(root)
    p2.pack(pady=100)
    c=Label(p2,text="1. shutdown /s	Shut down PC immediately",font="cosmic 15 italic",fg="black")
    c.pack()

    d=Label(p2,text="2. shutdown /r	Restarts   PC   immediately",font="cosmic 15 italic",fg="black")
    d.pack(pady=20)

    e=Label(p2,text="3. shutdown /a	 Aborts  Computer Process ",font="cosmic 15 italic",fg="black")
    e.pack()

    f=Label(p2,text="4. shutdown /h	  Hibernate PC immediately",font="cosmic 15 italic",fg="black")
    f.pack(pady=20)
    h=Label(p2,text="5. shutdown /f 	Forcely  Shutdowns  the PC",font="cosmic 15 italic",fg="black")
    h.pack()
    i=Label(p2,text="6. shutdown /l	  Logs  off  current  PC  user",font="cosmic 15 italic",fg="black")
    i.pack(pady=20)
    root.mainloop()


    


vamsi=Frame(root,bg="crimson");
vamsi.pack(padx=40,pady=100)

imag1e=ImageTk.PhotoImage(Image.open("c:\\Users\\haris\\Desktop\\New folder\\shut.png"))
kh=Button(vamsi,text="Shutdown",font="cosmic 10 italic",image=imag1e,compound=TOP,padx=70,pady=60,command=shut_down);
kh.grid(row=0,padx=30)

imag2e=ImageTk.PhotoImage(Image.open("c:\\Users\\haris\\Desktop\\New folder\\restart.png"))
kh1=Button(vamsi,text="Restart",font="cosmic 10 italic",image=imag2e,compound=TOP,padx=75,pady=60,command=shut_down);
kh1.grid(row=0,column=1,padx=40)

imag3e=ImageTk.PhotoImage(Image.open("c:\\Users\\haris\\Desktop\\New folder\\other.png"))
kh2=Button(vamsi,text="Other option",font="cosmic 10 italic",image=imag3e,compound=TOP,padx=62,pady=60,command=all_option);
kh2.grid(row=1,column=0,pady=40)

imag4e=ImageTk.PhotoImage(Image.open("c:\\Users\\haris\\Desktop\\New folder\\help.png"))
kh3=Button(vamsi,text="Help",font="cosmic 10 italic",image=imag4e,compound=TOP,padx=85,pady=60,command=Extra_Info);
kh3.grid(row=1,column=1,pady=40)
root.mainloop()
