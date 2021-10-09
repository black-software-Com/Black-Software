#!/use/bin/python3
# Black-Software v1.0                                                    
#  _____ _         _       _____     ___ _                     v1.0
# | __  | |___ ___| |_ ___|   __|___|  _| |_ _ _ _ ___ ___ ___ 
# | __ -| | .'|  _| '_|___|__   | . |  _|  _| | | | .'|  _| -_|
# |_____|_|__,|___|_,_|   |_____|___|_| |_| |_____|__,|_| |___|
                                                             
import os,subprocess,webbrowser,time,platform
from datetime import datetime
try:
    from tkinter import *
    from tkinter.ttk import Button as TButton,Entry, Separator
    from tkinter.messagebox import (showerror,askyesno)
    from tkinter.scrolledtext import ScrolledText
    from tkinter.colorchooser import askcolor
except (ImportError,ModuleNotFoundError):
    print("Installing...\n")
    subprocess.getoutput("pip install tk-tools")
    print("Setup...\n")
    time.sleep(4)
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip install colorama")
class Black_Software(Tk):
    def __init__(self):
        super(Black_Software,self).__init__()
        self.banner = """                                    
 _____ _         _       _____     ___ _                     v1.0
| __  | |___ ___| |_ ___|   __|___|  _| |_ _ _ _ ___ ___ ___  
| __ -| | .'|  _| '_|___|__   | . |  _|  _| | | | .'|  _| -_|
|_____|_|__,|___|_,_|   |_____|___|_| |_| |_____|__,|_| |___|
                                                             """
        self.time_zone = datetime.now()
        self.version = open("version.txt","r").read()
    def main(self):
        global label_s_g,soft_l,label_s 
        self.title('Black Software')
        self.banner = """                                    
 _____ _         _       _____     ___ _                     
| __  | |___ ___| |_ ___|   __|___|  _| |_ _ _ _ ___ ___ ___ 
| __ -| | .'|  _| '_|___|__   | . |  _|  _| | | | .'|  _| -_|
|_____|_|__,|___|_,_|   |_____|___|_| |_| |_____|__,|_| |___|
                                                             """
        soft_l = Label(self,text='black-software.ir')
        soft_l.pack(side = BOTTOM)
        label_s_g = Label(self,text=' ')
        label_s_g.pack()
        label_s_g.place(x=460,y=120)

        self.v_txt = f"""
{self.version} Installed!

Usage: <F5>
"""
        self.geometry("1000x795")
        self.ch = StringVar()
        label_s = Label(self,text='Search: ')
        label_s.pack()
        self.x = False
        self.end = '\033[0m'
        self.menu = Menu(self)
        self.filemenu = Menu(self.menu,tearoff=0)
        self.themefile = Menu(self.menu,tearoff=0)
        self.filemenu.add_command(label='Black',accelerator="F1",command=self.about)
        self.filemenu.add_command(label='Dev',accelerator="F2",command=self.developer)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',accelerator='Alt + F4',command=self.ext)
        self.themefile.add_command(label='Dark',command=self.dark)
        self.themefile.add_command(label='Light',command=self.light)
        self.themefile.add_separator()
        self.themefile.add_command(label='Customize',command=self.customize)
        self.menu.add_cascade(label='About',menu=self.filemenu)
        self.menu.add_cascade(label='Theme',menu=self.themefile)
        
        self.config(menu=self.menu)
        self.search = Entry(self,width=25,textvariable=self.ch)
        self.search.pack()
        self.search_button = Button(self,text='Search',width=9,height=3,command=self.search_word)
        self.search_button.pack()
        self.search_button.place(bordermode=OUTSIDE,x=460,y=50)
        self.command_line = Button(self,text='Shell',width=30,height=3,command=self.shell)
        self.command_line.pack()
        self.command_line.place(bordermode=OUTSIDE,x=390,y=230)
        self.github_b = Button(self,text='Github',width=9,height=3,command=self.github)
        self.github_b.pack()
        self.github_b.place(bordermode=OUTSIDE,x=380,y=300)
        self.instagram_b = Button(self,text='Instagram',width=9,height=3,command=self.instagram)
        self.instagram_b.pack()
        self.instagram_b.place(bordermode=OUTSIDE,x=460,y=300)
        self.web_b = Button(self,text='Website',width=9,height=3,command=self.website)
        self.web_b.pack()
        self.web_b.place(bordermode=OUTSIDE,x=540,y=300)
        self.exit = Button(self,text='Exit',width=9,height=3,command=self.ext)
        self.exit.pack()
        self.exit.place(bordermode=OUTSIDE,x=460,y=110)
        self.black_tool_b = Button(self,text='Black-Tool',width=9,height=3,command=self.black_tool)
        self.black_tool_b.pack()
        self.black_tool_b.place(bordermode=OUTSIDE,x=315,y=385)
        self.black_database_b = Button(self,text='Black-Database',width=12,height=3,command=self.black_database)
        self.black_database_b.pack()
        self.black_database_b.place(bordermode=OUTSIDE,x=400,y=385)
        self.black_attacker_b = Button(self,text='Data Attacker',width=12,height=3,command=self.black_attacker)
        self.black_attacker_b.pack()
        self.black_attacker_b.place(bordermode=OUTSIDE,x=500,y=385)
        self.black_instagram_b = Button(self,text='Black-Instagram',width=12,height=3,command=self.black_instagram)
        self.black_instagram_b.pack()
        self.black_instagram_b.place(bordermode=OUTSIDE,x=600,y=385)
        self.bind("<F5>",lambda x: self.install_update(x))
        sep_main = Separator(self)
        sep_main.pack(fill='x')
        tool_b = TButton(self,text='Tools',command=self.tool)
        tool_b.pack()
        tool_b.place(bordermode=OUTSIDE,x=290,y=200)
        dev = TButton(self,text='Developer',command=self.developer)
        dev.pack()
        dev.place(bordermode=OUTSIDE,x=370,y=200)
        update_b = TButton(self,text='Update',command=self.update)
        update_b.pack()
        update_b.place(bordermode=OUTSIDE,x=450,y=200)
        about_b = TButton(self,text='About',command=self.about)
        about_b.pack()
        about_b.place(bordermode=OUTSIDE,x=530,y=200)
        quit_b = TButton(self,text='Quit',command=self.ext)
        quit_b.pack()
        quit_b.place(bordermode=OUTSIDE,x=610,y=200)
        sep_2 = Separator(self)
        sep_2.pack(fill='x')
        self.txt = ScrolledText(self,width=100,height=20)
        self.txt.pack()
        self.txt['state'] = "disabled"
        self.txt.place(bordermode=INSIDE,x=100,y=450)
        self.icon = PhotoImage(file = './Scr/black.png')
        self.maxsize(1200,800)
        self.minsize(800,500)
        self.bind("<F1>",lambda x: self.about_2(x))
        self.bind("<F2>",lambda x: self.developer_2(x))
        self.iconphoto(False,self.icon)
        self.mainloop()
    def black_instagram(self):
        self.txt['state'] = "normal"
        self.txt.insert(END,"Installing Black-Instagram\n")
        run_i = subprocess.getoutput("git clone https://github.com/black-software-com/Black-Instagram")
        self.txt.insert(END,run_i)
        self.txt['state'] = "disabled"
    def black_attacker(self):
        self.txt['state'] = "normal"
        self.txt.insert(END,"Installing Black-Attacker\n")
        run_i = subprocess.getoutput("git clone https://github.com/black-software-com/Black-Attacker")
        self.txt.insert(END,run_i)
        self.txt['state'] = "disabled"
    def black_database(self):
        self.txt['state'] = "normal"
        self.txt.insert(END,"Installing Black-Database\n")
        run_i = subprocess.getoutput("git clone https://github.com/black-software-com/Black-Database")
        self.txt.insert(END,run_i)
        self.txt['state'] = "disabled"
    def black_tool(self):
        self.txt['state'] = "normal"
        self.txt.insert(END,"Installing Black-Tool\n")
        run_i = subprocess.getoutput("git clone https://github.com/black-software-com/Black-Tool")
        self.txt.insert(END,run_i)
        self.txt['state'] = "disabled"
    def dark(self):
        self.config(background='black')
        self.github_b.config(bg='black',fg='green')
        self.search_button.config(bg='black',fg='green')
        self.exit.config(bg='black',fg='green')
        label_s.config(bg='black',fg='green')
        self.instagram_b.config(bg='black',fg='green')
        self.web_b.config(bg='black',fg='green')
        soft_l.config(bg='black',fg='green')
        self.black_instagram_b.config(bg='black',fg='green')
        self.black_database_b.config(bg='black',fg='green')
        self.black_tool_b.config(bg='black',fg='green')
        self.black_attacker_b.config(bg='black',fg='green')
        self.search.config(background='black',foreground='green')
        self.txt.config(bg='black',fg='green')
        self.command_line.config(bg='black',fg='green')
    def light(self):
        self.config(background='white')
        self.github_b.config(bg='white',fg='black')
        self.search_button.config(bg='white',fg='black')
        self.exit.config(bg='white',fg='black')
        label_s.config(bg='white',fg='black')
        self.instagram_b.config(bg='white',fg='black')
        self.web_b.config(bg='white',fg='black')
        soft_l.config(bg='white',fg='black')
        self.black_instagram_b.config(bg='white',fg='black')
        self.black_database_b.config(bg='white',fg='black')
        self.black_tool_b.config(bg='white',fg='black')
        self.black_attacker_b.config(bg='white',fg='black')
        self.txt.config(bg='white',fg='black')
        self.search.config(background='white',foreground='black')
        self.command_line.config(bg='white',fg='black')
    def website(self):
        webbrowser.open_new_tab('https://black-software.ir')
    def github(self):
        webbrowser.open_new_tab('https://github.com/black-software-com')
    def instagram(self):
        webbrowser.open_new_tab('https://instagram.com/mrprogrammer2938')
    def about(self):
        webbrowser.open_new_tab('')
    def about_2(self,x):
        webbrowser.open_new_tab('')
    def customize(self):
        self.color = askcolor(title='Choose Color')
        self.config(background=self.color[1])

    def install_update(self):
        self.ext_2()
        subprocess.getoutput("cd .. && rm -r Black-Software && git clone https://github.com/black-software-com/Black-Software && python install.py")
        print(self.v_txt)
    def developer(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def developer_2(self,x):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def ext_2(self):
        self.destroy()
    def tool(self):
        webbrowser.open_new_tab('')
    
    def update(self):
        global label_b
        if self.version == 'Black-Software v1.0':
            print(False)
            label_b = Label(self,text='There is no update')
            label_b.pack()
            label_b.place(bordermode=INSIDE,x=300,y=280)
            label_b.after(4000,self.del_l)
        else:
            subprocess.getoutput("cd .. && rm -r Black-Software && git clone https://github.com/black-software-com/Black-Software && python install.py")
            label_b = Label(self,text=self.v_txt)
            label_b.pack()
            label_b.place(bordermode=INSIDE,x=300,y=280)
            label_b.after(4000,self.del_l)
    def del_l(self):
        label_b.destroy()
    def try_again(self):
        try1 = input("\nDo You Want To Try Again? [y/n] ")
        if try1.lower() == 'y':
            self.shell()
        elif try1.lower() == 'n':
            self.ext3()
        else:
            self.try_again()
    def ext(self):
        self.destroy()
        self.quit()
        quit()

    def search_word(self):
        global sep
        if self.ch.get() == 'developer':
            if self.x == False:
                self.sep = Separator(self)
                self.xsep.pack(fill='x')
                label_s_g = Label(self,text='Sina Meysami')
                label_s_g.pack()
                label_s_g.place(x=460,y=120)
                self.x = True
            else:
                sep.destroy()
                sep = Separator(self)
                sep.pack(fill='x')
                label_s_g.config(text=" ")
                label_s_g = Label(self,text='Sina Meysami')
                label_s_g.pack()
                label_s_g.place(x=460,y=120)
        elif self.ch.get().lower():
            if self.x == False:
                sep = Separator(self)
                sep.pack(fill='x')
                q = askyesno(title='Black-Software',message=f'Cannot Found {self.ch.get()}! Do You Want Search On Google?')
                if q:
                    label_s_g = Label(self,text=' ')
                    label_s_g.pack()
                    label_s_g.place(x=460,y=120)
                    webbrowser.open_new_tab(f'https://www.google.com/search?q={self.ch.get()}')
                    self.x = True
                else:
                    print(False)
            else:
                sep.destroy()
                sep = Separator(self)
                q = askyesno(title='Black-Software',message=f'Cannot Found {self.ch.get()}! Do You Want Search On Google?')
                if q:
                    label_s_g = Label(self,text=' ')
                    label_s_g.pack()
                    label_s_g.place(x=460,y=120)
                    webbrowser.open_new_tab(f'https://www.google.com/search?q={self.ch.get()}')
                    self.x = True
                else:
                    print(False)
                sep.pack(fill='x')
                webbrowser.open_new_tab(f'https://www.google.com/search?q={self.ch.get()}')
    @staticmethod
    def cls():
        if platform.system() == 'Linux':
            os.system("clear")
        else:
            os.system("cls")
    @staticmethod
    def title_c():
        if platform.system() == 'Linux':
            os.system("printf '\033]2;Black-Software\a'")
        else:
            os.system("title Black-Software")
    def shell(self):
        self.txt['state'] = 'normal'
        self.txt.insert(END,f"Start Black-Software Shell At: {self.time_zone}\nCheck Terminal")
        self.txt['state'] = 'disabled'
        self.title_c()
        self.cls()
        print(self.banner)
        print("{1}.Tools")
        print("{2}.Search")
        print("{3}.Developer")
        print("{4}.About")
        print("{5}.Website")
        print("{6}.Github")
        print("{7}.Instagram")
        print("{99}.Exit")
        try:
            while True:
                command = input("\n(Black-Software)~# ")
                if command == '' or command == ' ':
                    self.shell()
                elif command == '1':
                    webbrowser.open_new_tab('https://github.com/black-software-com')
                    self.try_again()
                elif command == '2':
                    search_key = input("Search: ")
                    print()
                    webbrowser.open_new_tab(f'https://www.google.com/search?q={search_key}')
                    self.try_again()
                elif command == '3':
                    webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
                    self.try_again()
                elif command == '4':
                   webbrowser.open_new_tab('')
                   self.try_again()
                elif command == '5':
                    webbrowser.open_new_tab('black-software.ir')
                    self.try_again()
                elif command == '6':
                    webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
                    self.try_again()
                elif command == '7':
                    webbrowser.open_new_tab('https://instagram.com/mrprogrammer2938')
                    self.try_again()
                elif command == '99' or command.lower() == 'exit' or command.lower() == 'quit':
                    self.txt['state'] = 'normal'
                    self.txt.insert(END,f"Closed Black-Software Shell At: {self.time_zone}")
                    self.txt['state'] = 'disabled'
                    print("Stop...\n")
                    break;
                else:
                    self.cls()
                    print(f"{command} {Fore.RED} Not Found! {self.end}")
                    self.try_again()
        except (Exception,KeyboardInterrupt):
            print("Stop...\n")
            self.ext_2()
if __name__ == '__main__':
    window = Black_Software()
    window.title_c()
    window.cls()
    print(window.banner)
    print(f'Start Black-Software At: {window.time_zone}')
    window.main()