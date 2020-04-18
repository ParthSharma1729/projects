import sys
import pymysql
from tkinter import messagebox
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import StudentDemoproject_support
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    StudentDemoproject_support.set_Tk_var()
    top = Student_data (root)
    StudentDemoproject_support.init(root, top)
    root.mainloop()

w = None
def create_Student_data(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    StudentDemoproject_support.set_Tk_var()
    top = Student_data (w)
    StudentDemoproject_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_data():
    global w
    w.destroy()
    w = None

class Student_data:


    def quit_1(self,event):
        # self.lstStudent.delete('0', 'end')
        self.txtName.delete('1.0', 'end')
        self.txtRoll.delete('1.0', 'end')
        self.txtMarks.delete('1.0', 'end')
        self.Spinbox1.delete('0','end')
        self.Radiobutton1.deselect()

        self.Radiobutton2.deselect()
        self.sex = ''
    def ModifyStudent(self):
        roll = self.txtRoll.get('1.0', 'end-1c')
        name = self.txtName.get('1.0', 'end-1c')
        # name = str(name)
        self.mycursor = mysql.cursor()

        self.mycursor.execute("select * from student WHERE RNO =" + roll)



        self.myresult = self.mycursor.fetchall()

        self.lstStudent.delete(0, 'end')
        for x in self.myresult:
            self.lstStudent.insert(1, x)



    def deleteStudent(self):
        roll=self.txtRoll.get('1.0','end-1c')
        name=self.txtName.get('1.0','end')
        name=str(name)
        self.mycursor = mysql.cursor()






        # self.mycursor.execute("delete from student WHERE RNO =" + roll)
        self.mycursor.execute("delete from student WHERE Name =" + name)
        messagebox.showinfo('Deletion', 'The Student was deleted successfully')
        # self.mycursor.execute("delete from student WHERE Name =" + name)


        mysql.commit()
        self.showdetails()




    def MaleSelected(self):
        self.sex='M'
    def FemaleSelected(self):
        self.sex='F'


    def addStudent(self,event):
        name=str(self.txtName.get('1.0','end'))
        roll=str(self.txtRoll.get('1.0','end'))
        marks=str(self.txtMarks.get('1.0','end'))
        sex=self.sex
        age=str(self.Spinbox1.get())
        try:
            self.mycursor = mysql.cursor()
            insQuery="insert into student values(' "+name+"',' "+roll+"',' "+marks+"',' "+sex+"',' "+age+"')"
            self.mycursor.execute(insQuery)
            self.showdetails()


            mysql.commit()
            messagebox.showinfo('Adding Student info',"The Student with name "+name+" was added successfully")
        except Exception:
             messagebox.showerror('Error in adding','Error in adding student')





    def showdetails(self):
        try:

            self.mycursor = mysql.cursor()

            self.mycursor.execute("select * from student")
            self.myresult = self.mycursor.fetchall()
            self.lstStudent.delete(0, 'end')
            for x in self.myresult:
                self.lstStudent.insert(1,x)
        except Exception:
               messagebox.showerror('ERROR ','ERROR IN FETCHING DATA')


    def __init__(self, top=None):
        try:
            global mysql
            mysql = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="Student")


        except Exception:

            messagebox.showerror('Error','Error while creating database')


            '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x661+650+150")
        top.title("Student Data")
        top.configure(background="#d9d9d9")

        self.var=tk.IntVar()

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.1, rely=0.076, relheight=0.477, relwidth=0.825)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=495)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.141, rely=0.095, height=34, width=62)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''NAME''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.141, rely=0.254, height=34, width=90)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''ROLL NO.''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.141, rely=0.762, height=34, width=43)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''AGE''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.141, rely=0.413, height=34, width=72)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''MARKS''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.141, rely=0.571, height=34, width=39)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font11)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''SEX''')

        self.txtName = tk.Text(self.Frame1)
        self.txtName.place(relx=0.485, rely=0.095, relheight=0.108
                , relwidth=0.352)
        self.txtName.configure(background="white")
        self.txtName.configure(font=font9)
        self.txtName.configure(foreground="black")
        self.txtName.configure(highlightbackground="#d9d9d9")
        self.txtName.configure(highlightcolor="black")
        self.txtName.configure(insertbackground="black")
        self.txtName.configure(selectbackground="#c4c4c4")
        self.txtName.configure(selectforeground="black")
        self.txtName.configure(width=174)
        self.txtName.configure(wrap="word")
        self.txtName.bind('<Escape>',self.quit_1)


        self.txtMarks = tk.Text(self.Frame1)
        self.txtMarks.place(relx=0.485, rely=0.413, relheight=0.108
                , relwidth=0.352)
        self.txtMarks.configure(background="white")
        self.txtMarks.configure(font=font9)
        self.txtMarks.configure(foreground="black")
        self.txtMarks.configure(highlightbackground="#d9d9d9")
        self.txtMarks.configure(highlightcolor="black")
        self.txtMarks.configure(insertbackground="black")
        self.txtMarks.configure(selectbackground="#c4c4c4")
        self.txtMarks.configure(selectforeground="black")
        self.txtMarks.configure(width=174)
        self.txtMarks.configure(wrap="word")
        self.txtMarks.bind('<Escape>', self.quit_1)

        self.txtRoll = tk.Text(self.Frame1)
        self.txtRoll.place(relx=0.485, rely=0.254, relheight=0.108
                , relwidth=0.352)
        self.txtRoll.configure(background="white")
        self.txtRoll.configure(font=font9)
        self.txtRoll.configure(foreground="black")
        self.txtRoll.configure(highlightbackground="#d9d9d9")
        self.txtRoll.configure(highlightcolor="black")
        self.txtRoll.configure(insertbackground="black")
        self.txtRoll.configure(selectbackground="#c4c4c4")
        self.txtRoll.configure(selectforeground="black")
        self.txtRoll.configure(width=174)
        self.txtRoll.configure(wrap="word")
        self.txtRoll.bind('<Escape>', self.quit_1)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.485, rely=0.571, relheight=0.111
                , relwidth=0.354)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=175)

        self.Radiobutton1 = tk.Radiobutton(self.Frame2)
        self.Radiobutton1.place(relx=0.057, rely=0.0, relheight=0.886
                , relwidth=0.383)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''MALE''')
        self.Radiobutton1.configure(variable=self.var,value=1,command=self.MaleSelected)

        self.Radiobutton2 = tk.Radiobutton(self.Frame2)
        self.Radiobutton2.place(relx=0.457, rely=0.0, relheight=0.886
                , relwidth=0.469)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''FEMALE''')
        self.Radiobutton2.configure(variable=self.var, value=2, command=self.FemaleSelected)

        self.Spinbox1 = tk.Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.485, rely=0.762, relheight=0.076
                , relwidth=0.356)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font=font9)
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=StudentDemoproject_support.spinbox)
        self.Spinbox1.bind('<Escape>', self.quit_1)
        self.Spinbox1.bind('<Return>', self.addStudent)

        self.btnShow = ttk.Button(top)
        self.btnShow.place(relx=0.1, rely=0.62, height=30, width=98)
        self.btnShow.configure(takefocus="")
        self.btnShow.configure(command=self.showdetails,text='''Show''')

        self.btnAdd = ttk.Button(top)
        self.btnAdd.place(relx=0.333, rely=0.62, height=30, width=98)
        self.btnAdd.configure(takefocus="")
        self.btnAdd.configure(command=self.addStudent,text='''Add''')

        self.btnModify = ttk.Button(top)
        self.btnModify.place(relx=0.55, rely=0.62, height=30, width=98)
        self.btnModify.configure(takefocus="")
        self.btnModify.configure(command=self.ModifyStudent,text='''Modify''')

        self.btnDelete = ttk.Button(top)
        self.btnDelete.place(relx=0.783, rely=0.62, height=30, width=98)
        self.btnDelete.configure(takefocus="")
        self.btnDelete.configure(command=self.deleteStudent,text='''Delete''')

        self.lstStudent = tk.Listbox(top)
        self.lstStudent.place(relx=0.1, rely=0.696, relheight=0.284
                , relwidth=0.823)
        self.lstStudent.configure(background="WHITE")
        self.lstStudent.configure(disabledforeground="#a3a3a3")
        self.lstStudent.configure(font=font10)
        self.lstStudent.configure(foreground="#000000")
        self.lstStudent.configure(width=494)

if __name__ == '__main__':
    vp_start_gui()





