import tkinter
import random
from tkinter import messagebox

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Student"

)
cur = mydb.cursor()
# s = "CREATE TABLE IF NOT EXISTS COLOR(Name varchar(20),Score integer(4))"
# cur.execute(s)

colours=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']

score=0

timeleft=30

def startgame(event):

                if timeleft==30:
                    countdown()


                nextcolor()

def nextcolor():
                global score
                global timeleft

                if timeleft > 0:
                                e.focus_set()


                                if e.get().lower() ==colours[1].lower():
                                                score+=1


                                e.delete(0, tkinter.END)
                else:
                    Msg = messagebox.askquestion('GAME OVER', 'DO YOU WANT TO CONTINUE')

                    try:
                        a = bs
                        b = score



                        root.destroy()

                        cur = mydb.cursor()
                        s = "INSERT INTO  COLOR (Name,Score) VALUES(%s,%s)"
                        b1 = (a, b)
                        cur.execute(s, b1)



                        mydb.commit()

                        rot = tkinter.Tk()

                        rot.title(' Score')
                        rot.geometry("434x75")

                        lstStudent = tkinter.Listbox(rot)
                        lstStudent.place(relx=0.043, rely=0.52, relheight=0.455, relwidth=0.935)
                        lstStudent.configure(background="white")
                        lstStudent.configure(disabledforeground="#a3a3a3")

                        lstStudent.configure(foreground="#000000")
                        lstStudent.configure(width=434)
                        lstStudent.configure(height=434)

                        mycursor = mydb.cursor()

                        mycursor.execute("select max(score),name from color")
                        myresult = mycursor.fetchall()
                        lstStudent.delete(0, 'end')
                        for x in myresult:
                            lstStudent.insert(1, x)




                        rot.mainloop()



                    except ValueError:
                        messagebox.showinfo("Error", "Please Input in Correcr Way")





                    if Msg == 'yes':
                        timeleft = 30
                        score = 0
                        e.delete(0, tkinter.END)
                        startgame

                    else:
                        exit()
                        root.destroy()




                random.shuffle(colours)

  


                label.config(fg=str(colours[1]), text=str(colours[0]))


                scorelabel.config(text= "Score: " + str (score))


def countdown():
                global timeleft


                if timeleft >0:
                    timeleft-=1



                    timelabel.config(text= "Time Left: " + str(timeleft))


                    timelabel.after(1000, countdown)

def colorgame(event):

    global timelabel
    global e
    global bs
    global label
    global scorelabel
    global root


    root=tkinter.Tk()


    bs=entry0.get()

    root.title('Hii '+bs)

    rooot.destroy()

    root.geometry("375x200")


    instructions=tkinter.Label(root,text="Type in the color of the words, and not the word text!",font=('Helvetica',12))


    instructions.pack()

    scorelabel= tkinter.Label(root,text="Press enter to start",font=('Helvetica',12))


    scorelabel.pack()

    timelabel = tkinter. Label(root, text= "Time Left: " + str(timeleft), font= ('Helvetica',12))

    timelabel.pack()


    label= tkinter.Label(root, font= ('Helvetica',60))

    label.pack()

    e= tkinter.Entry(root)

    root.bind('<Return>',startgame)

    e.pack()

    e.focus_set()



rooot = tkinter.Tk()

rooot.title("COLORGAME")

rooot.geometry("245x40")
rooot.resizable(0,0)

Label= tkinter.Label(rooot,text='Name',width=10)
Label.grid(row=0,column=0)

entry0= tkinter.Entry(rooot,width=25)
# entry0.config(textvariable=StringVar())
entry0.grid(column=1,row=0)

entry0.bind('<Return>',colorgame)

rooot.mainloop()
