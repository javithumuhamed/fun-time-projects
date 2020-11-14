import tkinter as tk
from tkinter import filedialog , Text
import os
selected=[]
current=[]

def apps():
    for widget in frame.winfo_children():
        widget.destroy()
    filename=filedialog.askopenfilename(initialdir="C:",title="Select File",
    filetypes=(("executabke","*.exe"),("All Files","*.*")))
    if(filename!=''):    
        selected.append(filename)
    for i in selected:
        if (i==''):
            continue
        else:
            label=tk.Label(frame,text=i,fg="black")
            label.pack()
def runa():
    for app in selected:
        os.startfile(app)

root=tk.Tk()
       

canvas=tk.Canvas(root,height=500,width=500,bg="#263D42")
canvas.pack()

frame=tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,rely=0.1,relx=0.1)
openf=tk.Button(root,command=apps,text="OPEN", padx=20,pady=5,fg="Green",bg="Black")
run=tk.Button(root,text="RUN ",command=runa, padx=20,pady=5,fg="Green",bg="Black")
run.pack()
openf.pack()
if os.path.isfile("save.txt"):
    with  open("save.txt","r") as f :
        temp=[]
        temp=f.read()    
        selected =[x  for x in temp.split(",") if temp.strip()]
    for i in selected:
        if i=='':
            pass
        else:
            label=tk.Label(frame,text=i,fg="black")
            label.pack()


root.mainloop()
with open ('save.txt','w') as f:
    for app in selected:
        if (app==""):
            pass
        else:
            f.write(app+",")