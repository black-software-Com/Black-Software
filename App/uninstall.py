from tkinter import *
from tkinter.ttk import *
import time
import subprocess
import webbrowser
root = Tk()
root.title('Black-Software/Uninstalling')
x = 1
def uninstall_2():
    subprocess.getoutput("cd && rm -r Black-Software")
    pb['value'] += 65
    print(True)
    install_b.destroy()
    exit.config(text='Finish')
    exit.place(bordermode=OUTSIDE,x=120,y=100)
def uninstall():
    pb['value'] += 35
    print(True)
    pb.after(3000,uninstall_2)
def un():
    global pb
    pb = Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280,
    )
    pb.pack()
    pb.place(bordermode=INSIDE,x=10,y=60)
    pb.after(2000,uninstall)
def black(y):
    webbrowser.open_new_tab('https://black-software.ir')
def dev(c):
    webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
def black_2():
    webbrowser.open_new_tab('https://black-software.ir')
def dev_2():
    webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
def ext():
    root.destroy()
    root.quit()
    quit()
menu = Menu(root)
filemenu = Menu(menu,tearoff=0)
filemenu.add_command(label='Black',accelerator='F1',command=black_2)
filemenu.add_command(label='Dev',accelerator='F2',command=dev_2)
filemenu.add_separator()
filemenu.add_command(label='Exit',accelerator='Alt+F4',command=ext)
menu.add_cascade(label='About',menu=filemenu)
root.config(menu=menu)

icon = PhotoImage(file = 'black.png')
label_mess = Label(root,text='Black-Software')
label_mess.pack()
label_mess.place(bordermode=INSIDE,x=120,y=30)

install_b = Button(root,text='Uninstall',command=un)
install_b.pack()
install_b.place(bordermode=OUTSIDE,x=120,y=100)
exit = Button(root,text='Exit',command=ext)
exit.pack()
exit.place(bordermode=OUTSIDE,x=120,y=128)
black_l = Label(root,text='Black-Software')
black_l.pack(side = BOTTOM)
root.iconphoto(False,icon)
root.bind("<F1>",lambda x: black(x))
root.resizable(0,0)
root.geometry("300x200")
root.mainloop()