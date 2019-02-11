from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("TicTacToe-AutoFill")
root.geometry("210x280")
flag=True

def reset():
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "


def result(b):
    if(b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or
         b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
         b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
         b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
         b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
         b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or
         b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
         b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        tkinter.messagebox.showinfo("Finish","Player X won..!")
    elif(b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0" or
         b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0" or
         b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0" or
         b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0" or
         b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0" or
         b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0" or
         b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0" or
         b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0"):
        tkinter.messagebox.showinfo("Finish","Player 0 won..!")
    
def checker(b):
    global flag
    if(b["text"] == " " and flag == True):
        b["text"]="X"
        flag=False
        result(b)
    elif(b["text"] == " " and flag == False):
        b["text"]="0"
        flag=True
        result(b)
    

b1=Button(root,text=" ",height=3,width=5,command=lambda:checker(b1))
b2=Button(root,text=" ",height=3,width=5,command=lambda:checker(b2))
b3=Button(root,text=" ",height=3,width=5,command=lambda:checker(b3))
b4=Button(root,text=" ",height=3,width=5,command=lambda:checker(b4))
b5=Button(root,text=" ",height=3,width=5,command=lambda:checker(b5))
b6=Button(root,text=" ",height=3,width=5,command=lambda:checker(b6))
b7=Button(root,text=" ",height=3,width=5,command=lambda:checker(b7))
b8=Button(root,text=" ",height=3,width=5,command=lambda:checker(b8))
b9=Button(root,text=" ",height=3,width=5,command=lambda:checker(b9))

blist=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
p=0
for x in range(0,3):
    for y in range(0,3):
        blist[p].grid(row=x,column=y,sticky=N+S+W+E)
        p+=1

l=Label(text=" ",height=3,width=5)
l.grid(row=3,column=1)
bReset=Button(root,text="Reset",height=3,width=5,command=reset)
bReset.grid(row=4,column=1)

root.mainloop()
