from tkinter import*
from tkinter.messagebox import *
from tkinter import font
import pymysql
from PIL import ImageTk, Image
from tkinter import ttk
#from PyQt4 import QtGui

root=Tk()
root.wm_minsize(width=650,height=500)
root.wm_maxsize(width=650,height=500)
root.title('Movie Recommendation System')
appHighlightFont = font.Font(family='Times', size=15, weight='bold')
appHighlightFont1 = font.Font(family='Comic Sans MS', size=22, weight='bold')
appHighlightFont2 = font.Font(family='Times', size=18, weight='bold')

def x():
    con = pymysql.connect(host="Localhost", user="root", passwd="root", db="STUDENT")
    myCursor = con.cursor()
    sql = "INSERT INTO MOVIE VALUES(e1,e2,e3,e4,e5,e6)"
    try:
        myCursor.execute(sql)
        con.commit()
        print("Record is inserted")
    except:
        con.rollback()
        print("No effect")
    con.rollback()

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("D:/images2.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
e = Example(root)
e.pack(fill=BOTH, expand=YES)

#registration form for new user
def new_user():
    t=Toplevel() #creates Toplevel object
    t.wm_minsize(width=650, height=600)
    t.wm_maxsize(width=650, height=600)

    class Example(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)
            self.image = Image.open("D:/images3..jpg")
            self.img_copy = self.image.copy()
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background = Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)

        def _resize_image(self, event):
            new_width = event.width
            new_height = event.height
            self.image = self.img_copy.resize((new_width, new_height))
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)
    e = Example(t)
    e.pack(fill=BOTH, expand=YES)

#heading
    l2=Label(t,text="       REGISTRATION FORM       ",font=appHighlightFont2,fg='Blue',bg='Light Blue')
    l2.place(x=150,y=80)

    #first name
    entryText1 = StringVar()
    e1=Entry(t,textvariable=entryText1,fg='yellow',justify='center',bg='Steel blue')
    entryText1.set("First Name")
    e1.place(width=240,height=30,x=200,y=150)

    #last name
    entryText2 = StringVar()
    e2 = Entry(t, textvariable=entryText2, fg='yellow', justify='center', bg='Steel blue')
    entryText2.set("Last Name")
    e2.place(width=240, height=30, x=200, y=200)

    entryText3 = StringVar()
    e3 = Entry(t, textvariable=entryText3, fg='yellow', justify='center', bg='Steel blue')
    entryText3.set("Email-Id")
    e3.place(width=240, height=30, x=200, y=250)

    entryText4 = StringVar()
    e4 = Entry(t, textvariable=entryText4, fg='yellow', justify='center', bg='Steel blue')
    entryText4.set("Mobile No.")
    e4.place(width=240, height=30, x=200, y=300)

    entryText5=StringVar()
    e5=ttk.Combobox(t,textvariable=entryText5)
    e5.place(x=200, y=350,width=240, height=30)
    e5.config(values=('Select Language','English','Hindi','Telegu'))
    e5['state'] ='readonly'
    Entry(t).pack()
    style = ttk.Style()
    style.map('TCombobox', selectbackground=[('readonly', 'Steel blue')])

    entryText6 = StringVar()
    e6 = Entry(t, textvariable=entryText6, fg='yellow', justify='center', bg='Steel blue')
    entryText6.set("Password")
    e6.place(width=240, height=30, x=200, y=400)

    e8 = Button(t, text="SUBMIT",borderwidth=8, font=appHighlightFont, fg='yellow', bg='Steel blue',command=x)
    e8.place(x=100, y=500, width=150, height=33)

    e9 = Button(t, text="LOGIN",borderwidth=8, font=appHighlightFont, fg='yellow', bg='Steel blue', command=registered_user)
    e9.place(x=400, y=500, width=150, height=33)

    t.mainloop()


#registered user
def registered_user():
    t1 = Toplevel()  # creates Toplevel object
    t1.wm_minsize(width=650, height=600)
    t1.wm_maxsize(width=650, height=600)

    class Example(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)
            self.image = Image.open("D:/images3..jpg")
            self.img_copy = self.image.copy()
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background = Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)

        def _resize_image(self, event):
            new_width = event.width
            new_height = event.height
            self.image = self.img_copy.resize((new_width, new_height))
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

    e = Example(t1)
    e.pack(fill=BOTH, expand=YES)

    # heading
    l2 = Label(t1, text="       LOGIN FORM       ", font=appHighlightFont2, fg='Blue', bg='Light Blue')
    l2.place(x=195, y=80)



    # first name
    entryText1 = StringVar()
    e1 = Entry(t1, textvariable=entryText1, fg='yellow', justify='center', bg='Steel blue')
    entryText1.set("EMAIL-ID")
    e1.place(width=240, height=30, x=200, y=250)

    # pass
    entryText2 = StringVar()
    e2 = Entry(t1, textvariable=entryText2, fg='yellow', justify='center', bg='Steel blue')
    entryText2.set("PASSWORD")
    e2.place(width=240, height=30, x=200, y=300)

    e3 = Button(t1, text="NEW REGISTER",borderwidth=8, font=appHighlightFont, fg='yellow', bg='Steel blue', command=new_user)
    e3.place(x=100, y=500, width=180, height=33)

    e4 = Button(t1, text="LOGIN",borderwidth=8, font=appHighlightFont, fg='yellow', bg='Steel blue', command=registered_user)
    e4.place(x=400, y=500, width=150, height=33)

    t1.mainloop()




#root part
l1=Label(root,text="WELCOME TO THE LOGIN FORM",font=appHighlightFont1,fg='Dark Green',bg='Yellow')
#l1(root,image="D:/images2.jpg",bg='grey').pack()
l1.place(x=85,y=30)

canvas = Canvas(root, width = 300, height = 200)
canvas.place(x=200,y=100)
img = ImageTk.PhotoImage(Image.open("D://user1.png"))
canvas.create_image(30, 10, anchor=NW, image=img)


#Creates Button for click on new user
b1=Button(root,text="NEW USER",borderwidth=8,font=appHighlightFont,width=15,height=2,fg='yellow',bg='#667C26',command=
new_user)
b1.place(x=225,y=300)

#Creates Button for click on Registered user
b2=Button(root,text="REGISTERED USER",borderwidth=8,font=appHighlightFont,width=25,height=2,fg='Yellow',bg='#667C26',command=registered_user)
b2.place(x=170,y=400)

root.mainloop()
