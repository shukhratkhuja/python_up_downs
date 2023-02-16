from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox
from datetime import datetime


class Student:
    def __init__(self,postgres):
        self.postgres=postgres
        self.postgres.title("Student Management System")

        self.postgres.geometry("1520x780+0+0")

        title=Label(self.postgres,text="TUIT Student Management System",bd=10,relief=GROOVE, font=('times new roman',40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #====All variables==#

        self.student_id_var = StringVar()
        self.fullname_var = StringVar()
        self.birthday_var = StringVar()
        self.gender_var = StringVar()
        self.department_var = StringVar()
        self.group_no_var = StringVar()
        self.phone_number_var = StringVar()
        self.email_var = StringVar()

        self.rec_id_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        Manage_Frame=Frame(self.postgres,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=540,height=660)
        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=('times new roman',30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Student ID",bg="crimson",fg="white",font=('times new roman',20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20, sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.student_id_var,font=('times new roman',15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20, ipadx=36, sticky="w")

        lbl_name = Label(Manage_Frame, text="Fullname", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.fullname_var, font=('times new roman', 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, ipadx=36, sticky="w")

        lbl_dept = Label(Manage_Frame, text="Birthday", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_dept.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_dept = Entry(Manage_Frame,textvariable=self.birthday_var, font=('times new roman', 15, "bold"), bd=5, relief=GROOVE)
        txt_dept.grid(row=3, column=1, pady=10, padx=20, ipadx=36, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame, textvariable=self.gender_var,font=('times new roman', 15, "bold"), state="readonly")
        combo_gender['values']=("male","female")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, ipadx=36, ipady=4, sticky="w")


        lbl_email = Label(Manage_Frame, text="Department", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_email.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame,textvariable=self.department_var, font=('times new roman', 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=5,column=1, padx=10, pady=10, ipadx=36)

        lbl_contact = Label(Manage_Frame, text="Group", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_contact= Entry(Manage_Frame,textvariable=self.group_no_var, font=('times new roman', 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=6, column=1, pady=10, padx=20, ipadx=36, sticky="w")

        lbl_dob = Label(Manage_Frame, text="Phone Number", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_dob.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, textvariable=self.phone_number_var,font=('times new roman', 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=7, column=1, pady=10, padx=20, ipadx=36, sticky="w")

        lbl_dob = Label(Manage_Frame, text="Email", bg="crimson", fg="white",
                         font=('times new roman', 20, "bold"))
        lbl_dob.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame, textvariable=self.email_var,font=('times new roman', 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=8, column=1, pady=10, padx=20, ipadx=36, sticky="w")



        #===Button===#
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=10, y=580, width=520)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students,bg="indigo",fg="white").grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data,bg="yellow",fg="black").grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data,bg="orange",fg="white").grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear,bg="green",fg="white").grid(row=0, column=3, padx=10, pady=10)


        # ===detail frame===#

        Detail_Frame = Frame(self.postgres, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=560, y=100, width=940, height=660)

        lbl_Search= Label(Detail_Frame, text="Search By", bg="crimson", fg="white",
                        font=('times new roman', 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, width=10,font=('times new roman', 13, "bold"), state="readonly")
        combo_search['values'] = ("Student ID","Fullname","Phone number")
        combo_search.set("Fullname")

        combo_search.grid(row=0, column=1, padx=10, pady=10, ipadx=36, ipady=4)

        txt_Search= Entry(Detail_Frame,textvariable=self.search_txt,width=20, font=('times new roman', 14, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=10, ipadx=48, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search",width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        #====Table Frame===#

        Table_Frame= Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=900, height=560)
        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("student_id","fullname","birthday","gender", "department","group_no", "phone_number","email", "created_date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("student_id",text="Student ID")
        self.Student_table.heading("fullname", text="Fullname")
        self.Student_table.heading("birthday", text="Birthday")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("department", text="Department")
        self.Student_table.heading("group_no", text="Group")
        self.Student_table.heading("phone_number", text="Phone Number")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("created_date", text="Created date")
        self.Student_table['show']='headings'
        self.Student_table.column("student_id",width=120)
        self.Student_table.column("fullname", width=200)
        self.Student_table.column("birthday", width=120)
        self.Student_table.column("gender", width=120)
        self.Student_table.column("department", width=200)
        self.Student_table.column("group_no", width=120)
        self.Student_table.column("phone_number", width=120)
        self.Student_table.column("email", width=200)
        self.Student_table.column("created_date", width=200)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def add_students(self):
        
        if (self.student_id_var.get()=="" or 
            self.fullname_var.get()=="" or 
            self.birthday_var.get() == "" or
            self.gender_var.get()=="" or 
            self.department_var.get()=="" or 
            self.group_no_var.get()=="" or 
            self.phone_number_var.get()=="" or 
            self.email_var.get()==""):

            messagebox.showerror("Error","All fields are required !!!")
        
        else:
            con=psycopg2.connect(host="localhost",user="postgres",password="p4stgr2s",dbname="tuit_sms")
            cur=con.cursor()
            
            cur.execute("SELECT exists (SELECT 1 FROM students WHERE student_id = '{}' LIMIT 1)".format(self.student_id_var.get()))
            is_exists = cur.fetchone()[0]
            if is_exists:
                messagebox.showerror("Error", f"Student with ID <{self.student_id_var.get()}> is already exists !")
            else:
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.student_id_var.get(),
                self.fullname_var.get(),
                self.birthday_var.get(),
                self.gender_var.get(),
                self.department_var.get(),
                self.group_no_var.get(),
                self.phone_number_var.get(),
                self.email_var.get(),
                datetime.now()
                ))
                messagebox.showinfo("Success","Records has been inserted !!!")
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()

    def fetch_data(self):
        con = psycopg2.connect(host="localhost", user="postgres", password="p4stgr2s", dbname="tuit_sms")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.student_id_var.set(""),
        self.fullname_var.set(""),
        self.birthday_var.set(""),
        self.gender_var.set(""),
        self.department_var.set(""),
        self.group_no_var.set(""),
        self.phone_number_var.set(""),
        self.email_var.set("")


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        print(row)
        self.student_id_var.set(row[0])
        self.fullname_var.set(row[1])
        self.birthday_var.set(row[2])
        self.gender_var.set(row[3])
        self.department_var.set(row[4])
        self.group_no_var.set(row[5])
        self.phone_number_var.set(row[6])
        self.email_var.set(row[7])

        self.rec_id_var.set(row[9])

    def update_data(self):
        con = psycopg2.connect(host="localhost", user="postgres", password="p4stgr2s", dbname="tuit_sms")
        cur = con.cursor()
        rec_id=self.rec_id_var.get()
        print(rec_id)
        query = "update students set student_id='{}', fullname='{}', birthday='{}'::date, gender='{}', department='{}', group_no='{}', phone_number='{}', email='{}' where rec_id={}::int".format(
        self.student_id_var.get(),
        self.fullname_var.get(),
        self.birthday_var.get(),
        self.gender_var.get(),
        self.department_var.get(),
        self.group_no_var.get(),
        self.phone_number_var.get(),
        self.email_var.get(),
        rec_id
        )
        print(query)
        cur.execute(query=query)
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):


        con = psycopg2.connect(host="localhost", user="postgres", password="p4stgr2s", dbname="tuit_sms")
        cur = con.cursor()
        
        print(type(self.student_id_var.get()))
        print(self.student_id_var.get())
        cur.execute("delete from students where student_id='{}'".format(self.student_id_var.get()))
        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo("Success", f"Student with ID <{self.student_id_var.get()}> has been deleted!!!")
        self.clear()

    def search_data(self):
        con = psycopg2.connect(host="localhost", user="postgres", password="p4stgr2s", dbname="tuit_sms")
        cur = con.cursor()

        sdict = {
            "Fullname": "fullname",
            "Student ID": "student_id",
            "Phone number": "phone_number"
        }
        
        cur.execute("select * from students where "+sdict[str(self.search_by.get())]+" ILIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
postgres=Tk()
ob=Student(postgres)
postgres.mainloop()