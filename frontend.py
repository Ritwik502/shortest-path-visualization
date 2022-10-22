import sys
sys.stdout = open('venv/inp.txt', 'w')
from tkinter import *

root=Tk()
root.title('Graph maker')
root.configure(background="#03d7fc")
root.geometry("600x650")
inputt=Label(root,text='Entre edge data here \n',font=("Arial", 25),background="#03d7fc")
inputt.pack()
cho=''

def get_text():
    for i in range(4):
        data = my_text[i].get(0.0, END)
        cho = data
        print(data,end='')
    root.destroy()
my_text=[None]*4

inputt=Label(root,text='(no. of nodes)',background="#03d7fc")
inputt.pack()
my_text[0]=Text(root,width=40,height=1)
my_text[0].pack(pady=10)

inputt=Label(root,text='(no. of edges)',background="#03d7fc")
inputt.pack()
my_text[1]=Text(root,width=40,height=1)
my_text[1].pack(pady=10)

inputt=Label(root,text='Are you using 1 based indexing[Y/N]',background="#03d7fc")
inputt.pack()
my_text[2]=Text(root,width=40,height=1)
my_text[2].pack(pady=10)

inputt=Label(root,text='Enter each edge as\n (node1 node2 edge_weight)',background="#03d7fc")
inputt.pack()
my_text[3]=Text(root,width=40,height=10)
my_text[3].pack(pady=10)

button_frame=Frame(root)
button_frame.pack()
get_text_b=Button(button_frame,text="Enter",command=get_text)
get_text_b.grid(row=1,column=1)
root.mainloop()
