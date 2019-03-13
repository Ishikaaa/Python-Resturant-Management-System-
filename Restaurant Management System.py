# user-name -- Ishika , password -- password
from tkinter import *
from tkinter import messagebox
import sqlite3
import time
now = time.strftime("%A %B %d %Y %H:%M:%S ")
a=Tk()
width, height = a.winfo_screenwidth(), a.winfo_screenheight()
a.geometry('%dx%d'%(width, height))
u=StringVar();p=StringVar();sum=IntVar()
ee1 = IntVar();ee2 = IntVar();ee3 = IntVar();ee4 = IntVar();ee5 = IntVar();ee6 = IntVar();ee7 = IntVar();ee8 = IntVar();ee9 = IntVar();ee10 = IntVar();ee11 = IntVar();ee12 = IntVar()
z1=StringVar();z2=StringVar();z3=StringVar();z4=StringVar();z5=StringVar();z6=StringVar();z7=StringVar();z8=StringVar();z9=StringVar();z10=StringVar()
z11=StringVar();z12=StringVar();z13=StringVar();z14=StringVar();z15=StringVar();z16=StringVar();z17=StringVar();z18=StringVar();z19=StringVar();z20=StringVar()
z21=StringVar();z22=StringVar();z23=StringVar();z24=StringVar()
AA=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# database
def bubu3():
    conn = sqlite3.connect("pro.db")
    conn.execute('''CREATE TABLE RMS1
       (DATE_TIME                    CHAR(50)       NOT NULL,
        ORDER_                    CHAR(50)       NOT NULL,
        PLAIN PRANTHA           CHAR(50),
        ALOO PRANTHA            CHAR(50),
        PANEER PRANTHA          CHAR(50),
        AJWAIN PRANTHA          CHAR(50),
        RAJMA CHAVAL            CHAR(50),
        CHANE CHAVAL            CHAR(50),
        KADI CHAVAL             CHAR(50),
        DAL CHAVAL              CHAR(50),
        DAL_ROTI                CHAR(50),
        CHANE_ROTI              CHAR(50),
        DAL_TANDOORI ROTI       CHAR(50),
        DAL_RUMALI ROTI         CHAR(50),
        CHEESE CHILLI           CHAR(50),
        MUSHROOM CHILLI         CHAR(50),
        MANCHURIAN              CHAR(50),
        SPRING ROLL             CHAR(50),
        CHICKEN SPRING ROLL     CHAR(50),
        CHILLI CHIKEN           CHAR(50),
        BONELESS CHILLI CHICKEN CHAR(50),
        LEMON CHICKEN           CHAR(50),
        TEA                     CHAR(50),
        HOT COFFEE              CHAR(50),
        COLD COFFEE             CHAR(50),
        BLACK COFFEE             CHAR(50))''')
    conn.execute(
        'INSERT INTO RMS1 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(now,ee1.get(),str(AA[0]), str(AA[1]), str(AA[2]),str(AA[3]),str(AA[4]),str(AA[5]),
                                                                                       str(AA[6]), str(AA[7]), str(AA[8]),str(AA[9]),str(AA[10]),str(AA[11]),str(AA[12]),
                                                                                       str(AA[13]), str(AA[14]),str(AA[15]),str(AA[16]),str(AA[17]),str(AA[18]), str(AA[19]),
                                                                                       str(AA[20]),str(AA[21]),str(AA[22]),str(AA[23])))
    conn.commit()
    a.destroy()

c = 0
# for login
def show2():
    global c
    a.geometry("380x220+450+250")
    F2=Frame(a,bg="bisque3");F2.grid(row=0,column=0)
    c+=1
    def show():
        u1 = u.get();p1 = p.get()
        if (u1 == "Ishika" and p1 == "password"):
            show10()
            a.mainloop()
        else:
            messagebox.showinfo("-- ERROR --", "Wrong Password. Please Enter right username and password",icon="warning")
            show2()
    if(c==6):
        # import simpleaudio as sa
        # wave_obj = sa.WaveObject.from_wave_file("who-are-you.wav")
        # play_obj = wave_obj.play()
        # play_obj.wait_done()
        a.quit()
    L11 = Label(F2, text="Username:", font="Verdana 15 bold",bg="bisque3");L11.grid(row=0, column=0,pady=15,padx=15)
    L21 = Label(F2, text="Password:", font="Verdana 15 bold",bg="bisque3");L21.grid(row=1, column=0,pady=30)
    e11 = Entry(F2, textvariable=u, width=25,background = "gainsboro",bd=3,cursor="dot");e11.grid(row=0, column=1,padx=40,pady=10);e11.delete(0, 'end')
    e21 = Entry(F2, show="*", textvariable=p, width=25,background = "gainsboro",bd=3,cursor="dot");e21.grid(row=1, column=1,padx=40,pady=10);e21.delete(0, 'end')
    B11 = Button(F2, text="Login", width=17, command=show, font="Verdana 17 bold", relief = RAISED,bg="bisque3");B11.grid(row=3, columnspan=2,pady=10)

# list of all menues
def bubu4():
    DD=Tk()
    DD.geometry("600x700")
    DD.title("Menu")
    FF10 = Frame(DD, height=400, width=400);FF10.grid(row=1, column=0)
    FF4 = Frame(DD, height=400, width=400);FF4.grid(row=0, column=0)
    FF5 = Frame(DD, height=400, width=400);FF5.grid(row=0, column=0)
    FF6 = Frame(DD, height=400, width=400);FF6.grid(row=0, column=0)
    FF7 = Frame(DD, height=400, width=400);FF7.grid(row=0, column=0)
    FF8 = Frame(DD, height=400, width=400);FF8.grid(row=0, column=0)
    FF9 = Frame(DD, height=400, width=400);FF9.grid(row=0, column=0)
    def show4():
        FF5.destroy();FF6.destroy();FF7.destroy();FF8.destroy();FF9.destroy()
        FF4 = Frame(DD,height=400,width=400);FF4.grid(row=0, column=0)
        LD1 = Label(FF4, text="Breakfast Meal", font="Courier 30 bold");LD1.grid(row=0, column=0, columnspan=3, padx=150)
        LD2 = Label(FF4, text="Plain Prantha", font="Consolas 10 bold");LD2.grid(row=1, column=0, pady=15);LR2 = Label(FF4, text="Rs 30");LR2.grid(row=1, column=1);ED1 = Entry(FF4, width=10, textvariable=z1);ED1.grid(row=1, column=2);ED1.insert(END, 0)
        LD3 = Label(FF4, text="Aloo Prantha", font="Consolas 10 bold");LD3.grid(row=2, column=0, pady=15);LR3 = Label(FF4, text="Rs 40");LR3.grid(row=2, column=1);ED2 = Entry(FF4, width=10, textvariable=z2);ED2.grid(row=2, column=2);ED2.insert(END, 0)
        LD4 = Label(FF4, text="Paneer Prantha", font="Consolas 10 bold");LD4.grid(row=3, column=0, pady=15);LR4 = Label(FF4, text="Rs60");LR4.grid(row=3, column=1);ED3 = Entry(FF4, width=10, textvariable=z3);ED3.grid(row=3, column=2);ED3.insert(END, 0)
        LD5 = Label(FF4, text="Ajwain Prantha", font="Consolas 10 bold");LD5.grid(row=4, column=0, pady=15);LR5 = Label(FF4, text="Rs 30");LR5.grid(row=4, column=1);ED4 = Entry(FF4, width=10, textvariable=z4);ED4.grid(row=4, column=2);ED4.insert(END, 0)
        def show44():
            print(ED1.get(),ED2.get(),ED3.get(),ED4.get())
            sum4 = int(ED1.get()) * 30 + int(ED2.get()) * 40 + int(ED3.get()) * 60 + int(ED4.get()) * 30
            AA[0]=int(ED1.get());AA[1]=int(ED2.get());AA[2]=int(ED3.get());AA[3]=int(ED4.get())
            ee2.set(sum4)
        def exit44():
            DD.destroy()
        BM4 = Button(FF4, text="Done", command=show44, width=20, height=2);BM4.grid(row=14, column=0, columnspan=3, pady=30)
        BM5 = Button(FF4, text="Exit", command=exit44, width=20, height=2);BM5.grid(row=15, column=0, columnspan=3, pady=30)
    def show5():
        FF4.destroy();FF6.destroy();FF7.destroy();FF8.destroy();FF9.destroy()
        FF5 = Frame(DD,height=400,width=400);FF5.grid(row=0, column=0)
        LD1 = Label(FF5, text="Meal", font="Courier 30 bold");LD1.grid(row=0, column=0, columnspan=3, padx=250)
        LD2 = Label(FF5, text="Rajma Chaval", font="Consolas 10 bold");LD2.grid(row=1, column=0, pady=15);LR2 = Label(FF5, text="Rs 30");LR2.grid(row=1, column=1);ED1 = Entry(FF5, width=10, textvariable=z5);ED1.grid(row=1, column=2);ED1.insert(END, 0)
        LD3 = Label(FF5, text="Chane Chaval", font="Consolas 10 bold");LD3.grid(row=2, column=0, pady=15);LR3 = Label(FF5, text="Rs 40");LR3.grid(row=2, column=1);ED2 = Entry(FF5, width=10, textvariable=z6);ED2.grid(row=2, column=2);ED2.insert(END, 0)
        LD4 = Label(FF5, text="Kadi Chaval", font="Consolas 10 bold");LD4.grid(row=3, column=0, pady=15);LR4 = Label(FF5, text="Rs 60");LR4.grid(row=3, column=1);ED3 = Entry(FF5, width=10, textvariable=z7);ED3.grid(row=3, column=2);ED3.insert(END, 0)
        LD5 = Label(FF5, text="Dal Chaval", font="Consolas 10 bold");LD5.grid(row=4, column=0, pady=15);LR5 = Label(FF5, text="Rs 30");LR5.grid(row=4, column=1);ED4 = Entry(FF5, width=10, textvariable=z8);ED4.grid(row=4, column=2);ED4.insert(END, 0)
        def show55():
            sum5 = int(ED1.get()) * 30 + int(ED2.get()) * 40 + int(ED3.get()) * 60 + int(ED4.get()) * 30
            AA[4] = int(ED1.get());AA[5] = int(ED2.get());AA[6] = int(ED3.get());AA[7] = int(ED4.get())
            ee3.set(sum5)
        BM5 = Button(FF5, text="Done", command=show55, width=20, height=2);BM5.grid(row=14, column=0, columnspan=3, pady=30)
    def show6():
        FF4.destroy();FF5.destroy();FF7.destroy();FF8.destroy();FF9.destroy()
        FF6 = Frame(DD,height=400,width=400);FF6.grid(row=0, column=0)
        LD1 = Label(FF6, text="Meal", font="Courier 30 bold");LD1.grid(row=0, column=0, columnspan=3, padx=250)
        LD2 = Label(FF6, text="Dal+Roti", font="Consolas 10 bold");LD2.grid(row=1, column=0, pady=15);LR2 = Label(FF6, text="Rs 30");LR2.grid(row=1, column=1);ED1 = Entry(FF6, width=10, textvariable=z9);ED1.grid(row=1, column=2);ED1.insert(END, 0)
        LD3 = Label(FF6, text="Chane+Roti", font="Consolas 10 bold");LD3.grid(row=2, column=0, pady=15);LR3 = Label(FF6, text="Rs 40");LR3.grid(row=2, column=1);ED2 = Entry(FF6, width=10, textvariable=z10);ED2.grid(row=2, column=2);ED2.insert(END, 0)
        LD4 = Label(FF6, text="Dal+Tandoori Roti", font="Consolas 10 bold");LD4.grid(row=3, column=0, pady=15);LR4 = Label(FF6, text="Rs 60");LR4.grid(row=3, column=1);ED3 = Entry(FF6, width=10, textvariable=z11);ED3.grid(row=3, column=2);ED3.insert(END, 0)
        LD5 = Label(FF6, text="Dal+Rumai Roti", font="Consolas 10 bold");LD5.grid(row=4, column=0, pady=15);LR5 = Label(FF6, text="Rs 30");LR5.grid(row=4, column=1);ED4 = Entry(FF6, width=10, textvariable=z12);ED4.grid(row=4, column=2);ED4.insert(END, 0)
        def show66():
            sum6 = int(ED1.get()) * 30 + int(ED2.get()) * 40 + int(ED3.get()) * 60 + int(ED4.get()) * 30
            AA[8] = int(ED1.get());AA[9] = int(ED2.get());AA[10] = int(ED3.get());AA[11] = int(ED4.get())
            ee4.set(sum6)
        BM56 = Button(FF6, text="Done", command=show66, width=20, height=2);BM56.grid(row=14, column=0, columnspan=3, pady=30)
    def show7():
        FF4.destroy();FF5.destroy();FF6.destroy();FF8.destroy();FF9.destroy()
        FF7 = Frame(DD);FF7.grid(row=0, column=0)
        LD1 = Label(FF7, text="Veg Snacks", font="Courier 30 bold");LD1.grid(row=0, column=0, columnspan=3, padx=150)
        LD2 = Label(FF7, text="Cheese Chilli", font="Consolas 10 bold");LD2.grid(row=1, column=0, pady=15);LR2 = Label(FF7, text="Rs 152");LR2.grid(row=1, column=1);ED1 = Entry(FF7, width=10, textvariable=z13);ED1.grid(row=1, column=2);ED1.insert(END, 0)
        LD3 = Label(FF7, text="Mushroom Chilli", font="Consolas 10 bold");LD3.grid(row=2, column=0, pady=15);LR3 = Label(FF7, text="Rs 152");LR3.grid(row=2, column=1);ED2 = Entry(FF7, width=10, textvariable=z14);ED2.grid(row=2, column=2);ED2.insert(END, 0)
        LD4 = Label(FF7, text="Manchurian", font="Consolas 10 bold");LD4.grid(row=3, column=0, pady=15);LR4 = Label(FF7, text="Rs 136");LR4.grid(row=3, column=1);ED3 = Entry(FF7, width=10, textvariable=z15);ED3.grid(row=3, column=2);ED3.insert(END, 0)
        LD5 = Label(FF7, text="Spring Roll", font="Consolas 10 bold");LD5.grid(row=4, column=0, pady=15);LR5 = Label(FF7, text="Rs 72");LR5.grid(row=4, column=1);ED4 = Entry(FF7, width=10, textvariable=z16);ED4.grid(row=4, column=2);ED4.insert(END, 0)
        def show77():
            sum7 = int(ED1.get()) * 152 + int(ED2.get()) * 152 + int(ED3.get()) * 136 + int(ED4.get()) * 72
            AA[12] = int(ED1.get());AA[13] = int(ED2.get());AA[14] = int(ED3.get());AA[15] = int(ED4.get())
            ee5.set(sum7)
        BM7 = Button(FF7, text="Done", command=show77, width=20, height=2);BM7.grid(row=14, column=0, columnspan=4, pady=30)
    def show8():
        FF4.destroy();FF5.destroy();FF6.destroy();FF7.destroy();FF9.destroy()
        FF8 = Frame(DD,height=400,width=400);FF8.grid(row=0, column=0)
        LD1 = Label(FF8, text="Non-Veg Snacks", font="Courier 30 bold");LD1.grid(row=0, column=0, columnspan=3, padx=100)
        LD2 = Label(FF8, text="Chicken Spring Roll", font="Consolas 10 bold");LD2.grid(row=1, column=0, pady=15);LR2 = Label(FF8, text="Rs 120");LR2.grid(row=1, column=1);ED1 = Entry(FF8, width=10, textvariable=z17);ED1.grid(row=1, column=2);ED1.insert(END, 0)
        LD3 = Label(FF8, text="Chilli Chiken", font="Consolas 10 bold");LD3.grid(row=2, column=0, pady=15);LR3 = Label(FF8, text="Rs 192");LR3.grid(row=2, column=1);ED2 = Entry(FF8, width=10, textvariable=z18);ED2.grid(row=2, column=2);ED2.insert(END, 0)
        LD4 = Label(FF8, text="Boneless Chilli Chiken", font="Consolas 10 bold");LD4.grid(row=3, column=0, pady=15);LR4 = Label(FF8, text="Rs 216");LR4.grid(row=3, column=1);ED3 = Entry(FF8, width=10, textvariable=z19);ED3.grid(row=3, column=2);ED3.insert(END, 0)
        LD5 = Label(FF8, text="Lemon Chicken", font="Consolas 10 bold");LD5.grid(row=4, column=0, pady=15);LR5 = Label(FF8, text="Rs 216");LR5.grid(row=4, column=1);ED4 = Entry(FF8, width=10, textvariable=z20);ED4.grid(row=4, column=2);ED4.insert(END, 0)
        def show88():
            sum8 = int(ED1.get()) * 120 + int(ED2.get()) * 192 + int(ED3.get()) * 216 + int(ED4.get()) * 216
            AA[16] = int(ED1.get());AA[17] = int(ED2.get());AA[18] = int(ED3.get());AA[19] = int(ED4.get())
            ee6.set(sum8)
        BM8 = Button(FF8, text="Done", command=show88, width=20, height=2);BM8.grid(row=14, column=0, columnspan=3, pady=30)
    def show9():
        FF4.destroy();FF5.destroy();FF6.destroy();FF7.destroy();FF8.destroy()
        FF9 = Frame(DD,height=400,width=400);FF9.grid(row=0, column=0)
        LD1 = Label(FF9, text="Drinks", font="Courier 30 bold");LD1.grid(row=0, column=0, columnspan=3, padx=250)
        LD2 = Label(FF9, text="Tea", font="Consolas 10 bold");LD2.grid(row=1, column=0, pady=15);LR2 = Label(FF9, text="Rs10");LR2.grid(row=1, column=1);ED1 = Entry(FF9, width=10, textvariable=z21);ED1.grid(row=1, column=2);ED1.insert(END, 0)
        LD3 = Label(FF9, text="Hot Coffee", font="Consolas 10 bold");LD3.grid(row=2, column=0, pady=15);LR3 = Label(FF9, text="Rs40");LR3.grid(row=2, column=1);ED2 = Entry(FF9, width=10, textvariable=z22);ED2.grid(row=2, column=2);ED2.insert(END, 0)
        LD4 = Label(FF9, text="Cold Coffee", font="Consolas 10 bold");LD4.grid(row=3, column=0, pady=15);LR4 = Label(FF9, text="Rs60");LR4.grid(row=3, column=1);ED3 = Entry(FF9, width=10, textvariable=z23);ED3.grid(row=3, column=2);ED3.insert(END, 0)
        LD5 = Label(FF9, text="Black Coffee", font="Consolas 10 bold");LD5.grid(row=4, column=0, pady=15);LR5 = Label(FF9, text="Rs30");LR5.grid(row=4, column=1);ED4 = Entry(FF9, width=10, textvariable=z24);ED4.grid(row=4, column=2);ED4.insert(END, 0)
        def show99():
            sum9 = int(ED1.get()) * 10 + int(ED2.get()) * 40 + int(ED3.get()) * 60 + int(ED4.get()) * 30
            AA[20] = int(ED1.get());AA[21] = int(ED2.get());AA[22] = int(ED3.get());AA[23] = int(ED4.get())
            ee7.set(sum9)
        BM9 = Button(FF9, text="Done", command=show99, width=20, height=2);BM9.grid(row=5, column=0, columnspan=3, pady=30)
    show4()
    BB4=Button(FF10,text="1",command=show4,width=10,height=4,bd=6, relief = RIDGE,bg="white");BB4.grid(row=0,column=0)
    BB5 = Button(FF10, text="2",command=show5,width=10,height=4,bd=6, relief = RIDGE,bg="white");BB5.grid(row=0, column=1)
    BB6 = Button(FF10, text="3",command=show6,width=10,height=4,bd=6, relief = RIDGE,bg="white");BB6.grid(row=0, column=2)
    BB7 = Button(FF10, text="4",command=show7,width=10,height=4,bd=6, relief = RIDGE,bg="white");BB7.grid(row=0, column=3)
    BB8 = Button(FF10, text="5",command=show8,width=10,height=4,bd=6, relief = RIDGE,bg="white");BB8.grid(row=0, column=4)
    BB9 = Button(FF10, text="6",command=show9,width=10,height=4,bd=6, relief = RIDGE,bg="white");BB9.grid(row=0, column=5)
def show10():
    f1 = Frame(a);f1.grid(row=0,column=0)
    width, height = a.winfo_screenwidth(), a.winfo_screenheight();a.geometry('%dx%d+0+0' % (width, height))
    def bubu1():
        sum = int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get())+int(e6.get())+int(e7.get());ee8.set(sum)
        st=(2/100)*sum;ee9.set(st)
        ta=(3/100)*sum;ee10.set(ta)
        sub=ta+20;ee11.set(sub)
        total=sum+sub;ee12.set(total)
    def bubu2():
        e1.delete(0,END);e1.insert(END, 0)
        e2.delete(0, END);e2.insert(END, 0)
        e3.delete(0, END);e3.insert(END, 0)
        e4.delete(0, END);e4.insert(END, 0)
        e5.delete(0, END);e5.insert(END, 0)
        e6.delete(0, END);e6.insert(END, 0)
        e7.delete(0,END);e7.insert(END, 0)
        e8.delete(0, END);e8.insert(END, 0)
        e9.delete(0, END);e9.insert(END, 0)
        e10.delete(0, END);e10.insert(END, 0)
        e11.delete(0, END);e11.insert(END, 0)
        e12.delete(0, END);e12.insert(END, 0)
    L1 = Label(f1, text="Resturant Management System", font="Courier 30 bold");L1.grid(row=0, columnspan=5, padx=350)
    L2 = Label(f1, text=now, font="Verdana 20 bold");L2.grid(row=1, columnspan=5, padx=350)
    L3 = Label(f1, text="Order No.", font="Courier 10 bold");L3.grid(row=3, pady=15);e1 = Entry(f1, textvariable=ee1);e1.grid(row=3, column=1, pady=15)
    L4 = Label(f1, text="Breakfast Meal", font="Courier 10 bold");L4.grid(row=4, pady=15);e2 = Entry(f1, textvariable=ee2);e2.grid(row=4, column=1, pady=15)
    L5 = Label(f1, text="Lumch Meal", font="Courier 10 bold");L5.grid(row=5, pady=15);e3 = Entry(f1, textvariable=ee3);e3.grid(row=5, column=1, pady=15)
    L6 = Label(f1, text="Dinne Meal", font="Courier 10 bold");L6.grid(row=6, pady=15);e4 = Entry(f1, textvariable=ee4);e4.grid(row=6, column=1, pady=15)
    L7 = Label(f1, text="Veg snacks", font="Courier 10 bold");L7.grid(row=7, pady=15);e5 = Entry(f1, textvariable=ee5);e5.grid(row=7, column=1, pady=15)
    L8 = Label(f1, text="Non-Veg Snacks", font="Courier 10 bold");L8.grid(row=8, pady=15);e6 = Entry(f1, textvariable=ee6);e6.grid(row=8, column=1, pady=15)
    L9 = Label(f1, text="Drinks", font="Courier 10 bold");L9.grid(row=3, column=2, pady=15);e7 = Entry(f1, textvariable=ee7);e7.grid(row=3, column=3, pady=15)
    L10 = Label(f1, text="cost", font="Courier 10 bold");L10.grid(row=4, column=2, pady=15);e8 = Entry(f1, textvariable=ee8);e8.grid(row=4, column=3, pady=15)
    L11 = Label(f1, text="Service Charge", font="Courier 10 bold");L11.grid(row=5, column=2, pady=15);e9 = Entry(f1, textvariable=ee9);e9.grid(row=5, column=3, pady=15)
    L12 = Label(f1, text="Tax", font="Courier 10 bold");L12.grid(row=6, column=2, pady=15);e10 = Entry(f1, textvariable=ee10);e10.grid(row=6, column=3, pady=15)
    L13 = Label(f1, text="Subtotal", font="Courier 10 bold");L13.grid(row=7, column=2, pady=15);e11 = Entry(f1, textvariable=ee11);e11.grid(row=7, column=3, pady=15)
    L14 = Label(f1, text="Total", font="Courier 10 bold");L14.grid(row=8, column=2, pady=15);e12 = Entry(f1, textvariable=ee12);e12.grid(row=8, column=3, pady=15)
    B1 = Button(f1, text="Total", width=25, bd=10,command=bubu1);B1.grid(row=9,column=1, pady=30)
    B2 = Button(f1, text="Reset", width=25,command=bubu2,bd=10,);B2.grid(row=9, column=2, pady=30)
    B3 = Button(f1, text="Menu", width=25,command=bubu4,bd=10,);B3.grid(row=9, column=0, pady=30)
    B4 = Button(f1, text="Exit", command=bubu3, width=25,bd=10,);B4.grid(row=9, column=3, pady=30)
    f1.grid(row=0, column=0)
show2()
a.mainloop()



# import pygame
# import time
# import random
#
# pygame.init()
#
# #crash_sound = pygame.mixer.Sound("crashhh.wav")
# pygame.mixer.music.load("racecar.mp3")
#
# display_width=1000
# display_height=600
#
# black=(0,0,0)
# white=(255,255,255)
# red=(100,0,0)
# green=(0,100,0)
# light_red=(255,0,0)
# light_green=(0,255,0)
# blue=(0,0,255)
# car_width=76
# car_height=99
#
# gameDisplay=pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('Race-4')
# clock=pygame.time.Clock()
#
# carImg=pygame.image.load('racercar1.png')
# bgImage=pygame.image.load('forest.png')
# gameIcon=pygame.image.load('carIcon.png')
# pygame.display.set_icon(gameIcon)
# pauseImg=pygame.image.load("police.png")
# crashImg=pygame.image.load("carcrashhh.png")
#
# pause=False
#
# def things_dodged(count):
#     font=pygame.font.SysFont(None,50)
#     text=font.render("Dodged: "+str(count),True,white)
#     gameDisplay.blit(text,(0,0))
#
# def things(thingx,thingy,thingw,thingh,color):
#     pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
#
# def car(x,y):
#     gameDisplay.blit(carImg,(x,y))
#
# def text_objects(text,font):
#     textSurface=font.render(text,True,blue)
#     return textSurface,textSurface.get_rect()
#
# def message_display(text):
#     largeText=pygame.font.SysFont("comicsansms",100)
#     TextSurf,TextRect=text_objects(text,largeText)
#     TextRect.center=((display_width/2.0),(display_height/7.0))
#     gameDisplay.blit(TextSurf,TextRect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#     game_loop()
#
# def crash():
#     pygame.mixer.music.stop()
#     #pygame.mixer.Sound.play(crash_sound)
#     gameDisplay.blit(crashImg,(0, 0))
#
#     largeText = pygame.font.SysFont("comicsansms", 100)
#     TextSurf, TextRect = text_objects('Oops! You Crashed', largeText)
#     TextRect.center = ((display_width / 2.0), (display_height / 7.0))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         button1('Play Again', 200, 450, 100, 50, green, light_green,game_loop)
#         button1('STOP!', 700, 450, 100, 50, red, light_red,quit)
#         pygame.display.update()
#         clock.tick(15)
#
# def unpaused():
#     global pause
#     pygame.mixer.music.unpause()
#     pause=False
#
# def paused():
#     pygame.mixer.music.pause()
#     gameDisplay.blit(pauseImg, (0, 0))
#
#     largeText = pygame.font.SysFont("comicsansms", 100)
#     TextSurf, TextRect = text_objects('paused', largeText)
#     TextRect.center = ((display_width / 2.0), (display_height / 7.0))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     while pause:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         button1('Continue', 200, 450, 100, 50, green, light_green,unpaused)
#         button1('STOP!', 700, 450, 100, 50, red, light_red,quit)
#         pygame.display.update()
#         clock.tick(15)
#
# def button1(msg,wb,y,w,h,ic,ac,action=None):
#     mouse = pygame.mouse.get_pos()
#     click=pygame.mouse.get_pressed()
#     if wb + w > mouse[0] > wb and y + h > mouse[1] > y:
#         pygame.draw.rect(gameDisplay,ac,(wb, y, w, h))
#         if click[0]==1 and action!=None:
#             action()
#     else:
#         pygame.draw.rect(gameDisplay,ic,(wb, y, w, h))
#
#     smallText = pygame.font.SysFont("comicsansms", 20)
#     TextSurf, TextRect = text_objects(msg, smallText)
#     TextRect.center = ((wb + (w / 2)),(y + (h / 2)))
#     gameDisplay.blit(TextSurf, TextRect)
#
#
# def game_intro():
#     intro=True
#     while intro:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#         gameDisplay.fill(black)
#         gameDisplay.blit(bgImage,(0,0))
#         largeText = pygame.font.SysFont("comicsansms", 100)
#         TextSurf, TextRect = text_objects('Race-4', largeText)
#         TextRect.center = ((display_width / 2.0), (display_height / 7.0))
#         gameDisplay.blit(TextSurf, TextRect)
#
#         button1('GO!', 200, 450, 100, 50, green, light_green,game_loop)
#         button1('STOP!', 700, 450, 100, 50, red, light_red,quit)
#         pygame.display.update()
#         clock.tick(15)
#
#
# def game_loop():
#     global pause
#     pygame.mixer.music.play(-1)
#     x=(display_width*0.45)
#     y=(display_height*0.63)
#     x_change=0
#     y_change=0
#
#     thing_startx=random.randrange(0,display_width)
#     thing_starty=-600
#     thing_speed=4
#     thing_width=100
#     thing_height=100
#
#     def things1(thingsx,thingsy,thingsw,thingsh,color):
#         pygame.draw.rect(gameDisplay,color,[thingsx,thingsy,thingsw,thingsh])
#
#     things_startx = 460
#     things_starty = 0
#     things_speed = 10
#     things_width = 30
#     things_height = 300
#     count=0
#     dodged=0
#
#     gameExit=False
#
#     while not gameExit:
#
#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type==pygame.KEYDOWN:
#                 if event.key==pygame.K_LEFT:
#                     x_change=-15
#                 if event.key==pygame.K_RIGHT:
#                     x_change=15
#                 if event.key==pygame.K_UP:
#                     y_change=-5
#                 if event.key==pygame.K_DOWN:
#                     y_change=5
#                 if event.key == pygame.K_p:
#                     pause=True
#                     paused()
#             if event.type==pygame.KEYUP:
#                 if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
#                     x_change=0
#                 if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
#                     y_change=0
#         x+=x_change
#         y+=y_change
#
#         gameDisplay.fill(white)
#         gameDisplay.blit(bgImage, (0, 0))
#
#         things(thing_startx,thing_starty,thing_width,thing_height,light_red)
#         thing_starty+=thing_speed
#         if count==120:
#             count=0
#             things_starty=0
#         count+=1
#         things1(things_startx, things_starty, things_width, things_height, black)
#         things_starty += things_speed
#
#         car(x,y)
#         things_dodged(dodged)
#
#         if x>display_width-car_width or x<1:
#             print(1)
#             crash()
#
#
#         if thing_starty>display_height:
#             thing_starty=0-thing_height
#             thing_startx=random.randrange(0,display_width-thing_width)
#             dodged+=1
#             thing_speed+=1
#
#
#         if y<thing_starty+thing_height:
#             print('y crossover')
#
#             if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
#                 print('x crossover')
#                 crash()
#
#
#         if y > display_height - car_height or y <1:
#             crash()
#
#         #if (y > thing_startx and y < thing_startx + thing_height) or (y + car_height > thing_startx + thing_height and y< thing_startx + thing_height):
#           #  crash()
#
#         pygame.display.update()
#         clock.tick(60)
# game_intro()
# game_loop()
# pygame.quit()
# quit()