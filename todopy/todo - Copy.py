import tkinter as tk
from tkinter import *
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical",command=canvas.yview)
        self.frame = ttk.Frame(canvas)
        self.frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        window = canvas.create_window((0, 0), window=self.frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True )
        scrollbar.pack(side="right", fill="y")

#####################
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
        with open('tasklist.txt',"w") as taskfile:
            taskfile.write("")
        for widget in frame3.frame.winfo_children():
            widget.pack_forget()
def addTask():
    task = task_entery.get()
    task_entery.delete(0,END)

    if task:
        with open("tasklist.txt","a")as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        
        box = ttk.Frame(frame3.frame, relief="ridge", borderwidth=2)
        box.pack(fill="x", padx=5, pady=2 )
        ttk.Label(box, text=f"{task_list[-1]}").pack(side="left", padx=5)
        ttk.Checkbutton(box,variable=tk.BooleanVar(value=False)).pack(side="right", padx=5)
def opentaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks :
            if task !='\n':
                task_list.append(task)
                for i in task_list:
                    box = ttk.Frame(frame3.frame, relief="ridge", borderwidth=2)
                    box.pack(fill="x", padx=5, pady=2)
                    ttk.Label(box, text=f"{i}").pack(side="left", padx=5)
                    ttk.Checkbutton(box,variable=tk.BooleanVar(value=True)).pack(side="right", padx=5 ,)
    except:
        file = open('tasklist.txt','w')
        file.close()   
   

###########################
frame = Frame(root,width=400 , height=50,bg="white").place(x = 0 , y = 500)
task = StringVar()
task_entery = Entry(frame,width=18,font="arial 20",bd=0)
task_entery.place(x =10,  y=500)
task_entery.focus()
button = Button(frame,text="ADD", font="arial 20 bold", width= 6,bg='#5a95ff' , fg="#fff",bd =0,command=addTask).place(x=300,y = 500)

frame3 = ScrollableFrame(root)
frame3.pack(fill="both", expand=False)


opentaskFile()
Button(root,image=delete,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()