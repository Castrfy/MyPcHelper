'''import libraries'''
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import os
import shutil
'''configure variables'''
os.chdir('assets')
path = os.getcwd()
shortcuts = list()
for i in os.listdir("shortcuts"):
    shortcuts.append(i)

firstikon = 0
secondikon = 0
thirdikon = 0
fourthikon = 0
shortcutswin = 0
Lb = 0
e = 0
scs = 0
entry1 = 0
entry2 = 0
button1 = 0
button2 = 0
hebutton0 = 0
hebutton1 = 0
hebutton2 = 0
hebutton3 = 0
exitbutton = 0
shortcutswin = 0
flag = True
entry3 = 0
entry4 = 0
def onClickedAna():
    global flag,button1,button2,exitbutton
    if flag == True:
        #########################################################
        '''configure AddButton'''
        button1 = tk.Toplevel()
        button1.geometry(f'30x30+{str(int(x+10))}+{str(int(y)-40)}')
        button1.overrideredirect(True)
        button1.attributes("-topmost", True)

        clickbutton3 = tk.Button(button1,
                                width=30,
                                image = addpicture,
                                height=30,
                                bg = "lightgreen",
                                activebackground="lightgreen",
                                command = onClickedAdd)
        clickbutton3.place(x=-3,y=-3)
        #########################################################
        '''configure PlayButton'''
        button2 = tk.Toplevel()
        button2.geometry(f'30x30+{str(int(x+10))}+{str(int(y)-80)}')
        button2.overrideredirect(True)
        button2.attributes("-topmost", True)

        clickbutton4 = tk.Button(button2,
                                width=30,
                                height=30,
                                image= playpicture,
                                bg = "lightgreen",
                                activebackground="lightgreen",
                                command = onClickedPlay)
        clickbutton4.place(x=-3,y=-3)

        #########################################################
        '''configure exitbutton'''
        exitbutton = tk.Toplevel()
        exitbutton.geometry(f'30x30+{str(int(x+10))}+{str(int(y)-120)}')
        exitbutton.overrideredirect(True)
        exitbutton.attributes("-topmost", True)

        clickbutton2 = tk.Button(exitbutton,
                                width=30,
                                image=closepicture,
                                compound=RIGHT,
                                height=30,
                                bg = "lightgreen",
                                activebackground="lightgreen",
                                command = onClickedExit,
                                text="."
                                )
        clickbutton2.place(x=-6.4,y=-4)

        #########################################################
        flag = False

        
    elif flag == False:
        button1.destroy()
        button2.destroy()
        exitbutton.destroy()
        flag = True



def findico():
    global shortcutswin,Lb,entry3
    if len(Lb.curselection()) != 0:
        fp = filedialog.askopenfilename(parent=shortcutswin,filetypes=[('PNG resmi', '*.png'),("JPEG resmi","*.jpg")])
        name = os.path.basename(fp)
        shutil.copy(fp,f"FastUses\icons\{str(int(Lb.get(Lb.curselection()[0]))-1)}.png")
        hekontrol()
    

def addsc():
    global entry1,entry2
    if entry2.get() != "":
        if entry1.get() != "":
            savefile=open(f"shortcuts//{str(entry1.get())}.txt","w")
            savefile.write(f"{str(entry2.get())}")
            savefile.close()
            
        
    

def onClickedHizliErisim():
    global Lb,entry3
    si= Lb.get(Lb.curselection()[0])
    if len(Lb.curselection()) != 0:
        if entry3.get() != "":
            savefile = open(f"FastUses//commands//{str(int(si)-1)}.txt","w")
            savefile.write(entry3.get())
            savefile.close()
            hekontrol()
        else:
            os.remove(f"FastUses//commands//{str(int(si)-1)}.txt")
            hekontrol()

def onClickedDelİco():
    global Lb
    si= Lb.get(Lb.curselection()[0])
    shutil.copy(f"FastUses\icons//backup.png",f"FastUses\icons\{str(int(Lb.get(Lb.curselection()[0]))-1)}.png")
    hekontrol()

def hekontrol():
    global hebutton0,hebutton1,hebutton2,hebutton3,firstikon,secondikon,thirdikon,fourthikon
    try:
        hebutton0.destroy()
        hebutton1.destroy()
        hebutton2.destroy()
        hebutton3.destroy()
    except:
        pass
    for i in os.listdir("FastUses/icons"):
        if i == "0.png":
            firstikon =  PhotoImage(file=f"FastUses/icons/{str(i)}").subsample(45,45)
        if i == "1.png":
            secondikon = PhotoImage(file=f"FastUses/icons/{str(i)}").subsample(45,45)
        if i == "2.png":
            thirdikon =  PhotoImage(file=f"FastUses/icons/{str(i)}").subsample(45,45)
        if i == "3.png":
            fourthikon =  PhotoImage(file=f"FastUses/icons/{str(i)}").subsample(45,45)
    if hebutton0 == 0:
        if hebutton1 == 0:
            if hebutton2 ==0:
                if hebutton3 ==0:
                    for i in os.listdir("FastUses/commands"):
                        file = open(f"FastUses/commands/{str(i)}","r")
                        if str(i)== "0.txt":
                            hebutton0 = tk.Toplevel(bg="lightgreen")
                            hebutton0.geometry(f"20x20+{str(int(x))}+{str(int(y+60))}")
                            hebutton0.overrideredirect(True)
                            hebutton0.attributes("-topmost", True)
                            b0=tk.Button(hebutton0,width=20,height=20,bg = "lightgreen",activebackground="lightgreen",command=onClickedHe0,image=firstikon)
                            b0.place(x=-2,y=-3)
                        elif str(i)== "1.txt":
                            hebutton1 = tk.Toplevel(bg="lightgreen")
                            hebutton1.geometry(f"20x20+{str(int(x+30))}+{str(int(y+60))}")
                            hebutton1.overrideredirect(True)
                            hebutton1.attributes("-topmost", True)
                            b1=tk.Button(hebutton1,width=20,height=20,bg = "lightgreen",activebackground="lightgreen",command=onClickedHe1,image=secondikon)
                            b1.place(x=-2,y=-3)
                        elif str(i)== "2.txt":
                            hebutton2 = tk.Toplevel(bg="lightgreen")
                            hebutton2.geometry(f"20x20+{str(int(x))}+{str(int(y+90))}")
                            hebutton2.overrideredirect(True)
                            hebutton2.attributes("-topmost", True)
                            b2=tk.Button(hebutton2,width=20,height=20,bg = "lightgreen",activebackground="lightgreen",command=onClickedHe2,image=thirdikon)
                            b2.place(x=-2,y=-3)
                        elif str(i)== "3.txt":
                            hebutton3 = tk.Toplevel(bg="lightgreen")
                            hebutton3.geometry(f"20x20+{str(int(x+30))}+{str(int(y+90))}")
                            hebutton3.overrideredirect(True)
                            hebutton3.attributes("-topmost", True)
                            b3=tk.Button(hebutton3,width=20,height=20,bg = "lightgreen",activebackground="lightgreen",command=onClickedHe3,image=fourthikon)
                            b3.place(x=-2,y=-3)

                else:
                    hebutton3.destroy()
                    hebutton3=0
                    hekontrol()
            else:
                 hebutton2.destroy()
                 hebutton2=0
                 hekontrol()
        else:
              hebutton1.destroy()
              hebutton1=0
              hekontrol()
    else:
        hebutton0.destroy()
        hebutton0=0
        hekontrol()
def closewin():
    global bayrak
    shortcutswin.destroy()
    bayrak = True
bayrak = True
def onClickedAdd():
    global entry1,entry2,shortcutswin,bayrak,entry3,entry4,zadd,Lb,shortcutswin
    if bayrak == True:  
        shortcutswin = tk.Toplevel()
        
        shortcutswin.title("Kısayol Ekle")
        shortcutswin.iconbitmap("ico1.ico")
        shortcutswin.protocol("WM_DELETE_WINDOW", closewin)
        shortcutswin.geometry(f"500x500+{int(screen_width/2 - 250)}+{int(y-225)}")
        
        icobutton = tk.Button(shortcutswin,width=2,height=1,text="+",bg="gray",activebackground="darkgray",command=findico)
        icobutton.place(x=170, y=380)
        label3 = tk.Label(shortcutswin,text="Icon Ekle")
        label3.place(x=110,y=383)
        label1000 = tk.Label(shortcutswin,text="(Dikkat! Icon resmi 1:1 ebatlarında olmalıdır)")
        label1000.place(x=80,y=410)
        
        entry1 = tk.Entry(shortcutswin,bg="lightgray",width=30)
        entry1.place(x=170,y=150)
        label1 = tk.Label(shortcutswin,text="Kısayol Adı")
        label1.place(x=100,y=150)

        label5 = tk.Label(shortcutswin,text="Uygulama Kısayolu")
        label5.place(x=210,y=108)
        
        entry2 = tk.Entry(shortcutswin,bg="lightgray",width=30)
        entry2.place(x=170,y=130)
        label2 = tk.Label(shortcutswin,text="Komut")
        label2.place(x=100,y=130)
        
        button123 = tk.Button(shortcutswin,text="Ekle",bg="gray",activebackground="darkgray",command = addsc)
        button123.place(x=245, y=180)

        label4 = tk.Label(shortcutswin,text="Hızlı Erişim")
        label4.place(x=230,y=326)
        
        entry3 = tk.Entry(shortcutswin,bg="lightgray",width=30)
        entry3.place(x=170,y=350)
        label3 = tk.Label(shortcutswin,text="Komut")
        label3.place(x=110,y=346)
        
        button3 = tk.Button(shortcutswin,text="Ayarla",bg="gray",activebackground="darkgray",command = onClickedHizliErisim)
        button3.place(x=240, y=380)

        delico = tk.Button(shortcutswin,text="Seçili butonun ikonunu sil",bg="darkgray",command = onClickedDelİco)
        delico.place(x=330,y=400)
        
        L2=tk.Label(shortcutswin,text="Düzenlenecek \nHızlı Erişim Numarası\n(silmek için komudu boş bırakın)")
        L2.place(x=315,y=270)
        Lb=tk.Listbox(shortcutswin,width=2,height=4,bg="gray")
        Lb.insert(1,"1")
        Lb.insert(2,"2")
        Lb.insert(3,"3")
        Lb.insert(4,"4")
        Lb.place(x=395,y=325)
        
        bayrak=False
    elif bayrak == False:
        shortcutswin.destroy()
        bayrak=True

def onClickedHe0():
    os.system(open("FastUses//commands//0.txt","r").read())

def onClickedHe1():
    os.system(open(f"FastUses//commands//1.txt","r").read())

def onClickedHe2():
    os.system(open(f"FastUses//commands//2.txt","r").read())

def onClickedHe3():
    os.system(open(f"FastUses//commands//3.txt","r").read())

def ondoubleclick(event):
    index = event.widget.curselection()[0]
    selected_item = event.widget.get(index)
    selected_item = str(selected_item) + ".txt"
    komut = open(f"shortcuts//{selected_item}","r")
    os.system(komut.read())
            
fllag= True
def onClickedPlay():
    global fllag,scs,shortcuts
    if fllag == True:
        scs= tk.Toplevel()
        scs.geometry(f"80x110+{int(x-80)}+{int(y-120)}")
        scs.overrideredirect(True)
        scs.attributes("-topmost",True)
        shortcuts = list()
        scroool = tk.Scrollbar(scs)
        shortcus = tk.Listbox(scs,yscrollcommand = scroool.set)
        for i in os.listdir("shortcuts"):
            shortcuts.append(i)
        row = 0
        for i in shortcuts:
            shortcus.insert(END,f'{os.path.splitext(i)[0]}')
            row+=1
        scroool.config( command = shortcus.yview )
        scroool.pack(side = LEFT,fill = Y)
        shortcus.bind('<Double-Button-1>', ondoubleclick)
        shortcus.pack(side = RIGHT,fill = BOTH)
        fllag = False
    elif fllag == False:
        scs.destroy()
        fllag = True


def onClickedExit():
    homebutton.destroy()


#########################################################
homebutton = tk.Tk()

'''configure variables'''
screen_width = homebutton.winfo_screenwidth()
screen_height = homebutton.winfo_screenheight()
x = screen_width-70
y = (screen_height/2) - (50/2)
closepicture = PhotoImage(file="exit.png").subsample(30,30)
homepicture = PhotoImage(file="home.png").subsample(18,18)
addpicture = PhotoImage(file="add.png").subsample(30,30)
playpicture = PhotoImage(file="play.png").subsample(30,30)
zadd = PhotoImage(file="zoomedadd.png").subsample(30,30)

#########################################################

'''configure homebutton'''
homebutton.geometry(f'50x50+{str(x)}+{str(int(y))}')
homebutton.overrideredirect(True)
homebutton.attributes("-topmost", True)

clickbutton1 = tk.Button(homebutton,
                        width=50,
                        height=50,
                        bg = "lightgreen",
                        image = homepicture,
                        activebackground="lightgreen",
                        command = onClickedAna)
clickbutton1.place(x=-2,y=-2)
'''configure FastUses'''

hekontrol()
    
homebutton.mainloop()
