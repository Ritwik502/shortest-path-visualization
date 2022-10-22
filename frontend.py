import sys
sys.stdout = open('venv/inp.txt', 'w')
from tkinter import *

root=Tk()
root.title('Graph maker')
root.configure(background="#03d7fc")
root.geometry("600x600")
inputt=Label(root,text='Entre edge data here in format\n (no. of nodes)\n(no. of edges)\nAre you using 1 based indexing[Y/N]\n(edge1)\n(edge2)\n.\n.\n.',background="#03d7fc")
inputt.pack(pady=10)
cho=''

def get_text():
    for i in range(4):
        data = my_text[i].get(0.0, END)
        cho = data
        print(data,end='')
    root.destroy()
my_text=[None]*4
my_text[0]=Text(root,width=60,height=1)
my_text[0].pack(pady=3)
my_text[1]=Text(root,width=60,height=1)
my_text[1].pack(pady=3)
my_text[2]=Text(root,width=60,height=1)
my_text[2].pack(pady=3)
my_text[3]=Text(root,width=60,height=10)
my_text[3].pack(pady=3)
button_frame=Frame(root)
button_frame.pack()
get_text_b=Button(button_frame,text="Enter",command=get_text)
get_text_b.grid(row=1,column=1)
root.mainloop()
