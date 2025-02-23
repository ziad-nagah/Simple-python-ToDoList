import tkinter
from tkinter import *

root = Tk()
root.title("todolist")
root.geometry("400x650+400+100")
root.resizable(False,False)

icon =  PhotoImage(file="note.png")
topbar= PhotoImage(file="topbar.png")
doc = PhotoImage(file="setting.png")
note = PhotoImage(file="note.png")
delete = PhotoImage(file="delete.png")
Label(root,image=topbar).pack()
Label(root,image=doc ,bg="#32405b").place(x = 30 , y = 25)
Label(root,image=note,bg="#32405b").place(x = 340 , y = 25)
Label(root,text="ALL Tasks" , font="arial 20 bold",fg="white",bg="#32405b").place(x = 130 , y = 20)
root.iconphoto(False,icon)
###########################
task_list = []
def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt',"w") as taskfile:
            taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
def addTask():
    task = task_entery.get()
    task_entery.delete(0,END)

    if task:
        with open("tasklist.txt","a")as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def opentaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks :
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file = open('tasklist.txt','w')
        file.close()   
   

###########################
frame = Frame(root,width=400 , height=50,bg="white").place(x = 0 , y = 180)
task = StringVar()
task_entery = Entry(frame,width=18,font="arial 20",bd=0)
task_entery.place(x =10,  y=190)
task_entery.focus()
button = Button(frame,text="ADD", font="arial 20 bold", width= 6,bg='#5a95ff' , fg="#fff",bd =0,command=addTask).place(x=300,y = 180)

frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady =(170,0))
listbox=Listbox(frame1,font =('arial',12),width=40,height=16 , bg="#32405b",fg="white",cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command=listbox.yview)
opentaskFile()
Button(root,image=delete,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()