from tkinter import*
from tkinter import ttk
import pymysql
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import os,random
from datetime import datetime
from tkinter import filedialog
from tkinter import Tk




class Student:
    def init(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.config(bg="white")

        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # ===============Images==================================

        # image1
        img10 = Image.open(r"C:\Users\Samch\Downloads\1st.jpg")
        img10 = img10.resize((510,160), Image.Resampling.LANCZOS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
      
        self.f_lbl_1=Button(self.root,command=self.openImg_1,image=self.photoImg10,cursor="hand2")
        self.f_lbl_1.place(x=(-10),y=0,width=545,height=160)
        
        # image2
        img11 = Image.open(r"C:\Users\Samch\Downloads\2nd.jpg")
        img11 = img11.resize((500,160), Image.Resampling.LANCZOS)
        self.photoImg11 = ImageTk.PhotoImage(img11)

        
        self.f_lbl_2=Button(self.root,command=self.openImg_2,image=self.photoImg11,cursor="hand2")
        self.f_lbl_2.place(x=515,y=0,width=500,height=160)

        # image3
        img13 = Image.open(r"C:\Users\Samch\Downloads\student.jpg")
        img13 = img13.resize((550,160), Image.Resampling.LANCZOS)
        self.photoImg13= ImageTk.PhotoImage(img13)
    
    
        self.f_lbl_3=Button(self.root,command=self.openImg_3,image=self.photoImg13,cursor="hand2")
        self.f_lbl_3.place(x=990,y=0,width=550,height=160)
       
        # ====================Background image==============================================
        img1 = Image.open(r"C:\Users\Samch\Downloads\university.jpg")
        img1 = img1.resize((1535,710), Image.Resampling.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=130,width=1535,height=710)

        Manage_std_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_std_frame.place(x=15,y=55,width=1500,height=600)

        # ==================== Project title ==================================================
        title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),bg="white",fg="blue")
        title.place(x=0,y=(-2),width=1550,height=50)

        img_logo = Image.open(r"C:\Users\Samch\Downloads\logo.png")
        img_logo = img_logo.resize((50,50), Image.Resampling.LANCZOS)
        self.photoImg_logo= ImageTk.PhotoImage(img_logo)
        bg_lbl=Label(bg_lbl,image=self.photoImg_logo,bd=20)
        bg_lbl.place(x=300,y=2,width=50,height=40)

        # =================time================================
        def time(): 
            string = strftime('%I:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(title, font = ('times new roman',16, 'bold'),background = 'white',foreground = 'blue') 
        lbl.place(x=0,y=(-15),width=120,height=50) 
        time()

        # =======Framedetails===================================================================================
        
        DataFrameLeft=LabelFrame(Manage_std_frame,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",
                                                font=("arial",12,"bold"),text="Student Information ")
        DataFrameLeft.place(x=10,y=10,width=660,height=580)

        #  ================Right labelframe=================
        DataFrameRight=LabelFrame(Manage_std_frame,bd=4,padx=2,relief=RIDGE,bg="white",fg="crimson",
                                                font=("arial",12,"bold"),text="Student Details")
        DataFrameRight.place(x=670,y=10,width=820,height=580)

        img30 = Image.open(r"C:\Users\Samch\Downloads\8th.jpg")
        img30 = img30.resize((650,120), Image.Resampling.LANCZOS)
        self.photoImg30 = ImageTk.PhotoImage(img30)
        myimg=Label(DataFrameLeft,image=self.photoImg30,bd=2,relief=RIDGE)
        myimg.place(x=0,y=(-3),width=650,height=120)

        img20 = Image.open(r"C:\Users\Samch\Downloads\3rd.jpg")
        img20 = img20.resize((810,200), Image.Resampling.LANCZOS)
        self.photoImg20 = ImageTk.PhotoImage(img20)
        bg_lbl=Label(DataFrameRight,image=self.photoImg20)
        bg_lbl.place(x=0,y=0,width=810,height=200)

        # Curent course Information labelFrame
        std_Info_label_frame=LabelFrame(DataFrameLeft,padx=10,bd=2,relief=RIDGE,font=("times new roman",11,"bold"),fg="darkgreen",bg="white",text="Current Course Information")
        std_Info_label_frame.place(x=1,y=100,width=650,height=115)

        # label and entries
        # department
        lbl_dep=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Department:",bg="white")
        lbl_dep.grid(row=0,column=0,sticky=W,padx=2,pady=10)
        com_dep=ttk.Combobox(std_Info_label_frame,textvariable=self.var_dep,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_dep['value']=("Select Department","Computer","Mechnical","Civil","Electonic","Electrical","Automobile","IT")
        com_dep.current(0)
        com_dep.grid(row=0,column=1,sticky=W,padx=2)

        # course
        course_std=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        com_txtcourse_std=ttk.Combobox(std_Info_label_frame,textvariable=self.var_course,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_txtcourse_std['value']=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

        # year
        currunt_year=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Year:",bg="white")
        currunt_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txt_currunt_year=ttk.Combobox(std_Info_label_frame,textvariable=self.var_year,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_txt_currunt_year['value']=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txt_currunt_year.current(0)
        com_txt_currunt_year.grid(row=1,column=1,sticky=W,padx=2)

        # semster
        label_Semester=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        comSemester=ttk.Combobox(std_Info_label_frame,textvariable=self.var_semester,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        comSemester['value']=("Select Semester","Semster-1","Semester-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # student_class_Information
        std_personalData_label_frame=LabelFrame(DataFrameLeft,padx=10,pady=5,bd=2,relief=RIDGE,font=("times new roman",11,"bold"),fg="darkgreen",bg="white",text="Student Class Information")
        std_personalData_label_frame.place(x=1,y=220,width=650,height=300)

        lbl_id=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="StudentID No:",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        txt_id=ttk.Entry(std_personalData_label_frame,textvariable=self.va_std_id,width=22,font=("arial",11,"bold"))
        txt_id.grid(row=0,column=1,padx=2,pady=7)

        lbl_Name=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Student Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(std_personalData_label_frame,textvariable=self.var_std_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        lbl_div=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(std_personalData_label_frame,textvariable=self.var_div,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        lbl_roll=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Roll No:",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_roll=ttk.Entry(std_personalData_label_frame,textvariable=self.var_roll,width=22,font=("arial",11,"bold"))
        txt_roll.grid(row=1,column=3,padx=2,pady=7)

        lbl_gender=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(std_personalData_label_frame,textvariable=self.var_gender,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        lbl_dob=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(std_personalData_label_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=7)

        lbl_email=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(std_personalData_label_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=7)

        lbl_phone=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(std_personalData_label_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)

        lbl_adderss=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_adderss.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_adderss=ttk.Entry(std_personalData_label_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_adderss.grid(row=4,column=1,padx=2,pady=7)

        lbl_teacher=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Teacher Name:",bg="white")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_teacher=ttk.Entry(std_personalData_label_frame,textvariable=self.var_teacher,width=22,font=("arial",11,"bold"))
        txt_teacher.grid(row=4,column=3,padx=2,pady=7)

        img301 = Image.open(r"C:\Users\Samch\Downloads\clg.jpg")
        img301 = img301.resize((330,100), Image.Resampling.LANCZOS)
        self.photoImg501 = ImageTk.PhotoImage(img301)
        youimg=Label(std_personalData_label_frame,image=self.photoImg501)
        youimg.place(x=(-10),y=200,width=330,height=100)

        img30 = Image.open(r"C:\Users\Samch\Downloads\clg.jpg")
        img30 = img30.resize((330,100), Image.Resampling.LANCZOS)
        self.photoImg50 = ImageTk.PhotoImage(img30)
        youimg=Label(std_personalData_label_frame,image=self.photoImg50)
        youimg.place(x=320,y=200,width=310,height=100)

        # ===========Buttonframe1================================================================================
        ButtonFrame1=Frame(DataFrameLeft,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=516,width=650,height=38)

      

        # ===================================ButtonFrame=====================================
        btnAddData=Button(ButtonFrame1,text="SAVE",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnUpdate=Button(ButtonFrame1,text="UPDATE",command=self.std_update,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(ButtonFrame1,text="DELETE",command=self.std_delete,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(ButtonFrame1,text="RESET",command=self.clear,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btnReset.grid(row=0,column=3,padx=1)

        # =======table&search=====================================================================================
        Table_frame=LabelFrame(DataFrameRight,text="View Student Details & Search System",font=("arial",11,"bold"),bg="white",bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=200,width=810,height=70)

        # ==========Search By========
        lblSearch=Label(Table_frame,font=("arial",15,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=2,sticky=W,padx=5)

        # variable
        self.serch_var=StringVar()
        search_combo=ttk.Combobox(Table_frame,width=12,textvariable=self.serch_var,font=("times new roman",15),state="readonly")
        search_combo['values']=("Select Option","Phone","Roll","Dep")
        search_combo.grid(row=0,column=3,sticky=W,padx=5)
        search_combo.current(0)

        self.serchTxt_var=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=16,textvariable=self.serchTxt_var,font=("times new roman",15))
        txtSearch.grid(row=0,column=4,padx=5)

        btnExit=Button(Table_frame,text="SEARCH",command=self.search_data,font=("arial",12,"bold"),width=14,bg="blue",fg="white")
        btnExit.grid(row=0,column=5,padx=5)

        btnExit=Button(Table_frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),width=13,bg="blue",fg="white")
        btnExit.grid(row=0,column=6,padx=5)

        # =======Room Table Scrollbar=====================================================================================
        Table_frame=Frame(DataFrameRight,bd=4,relief=RIDGE)
        Table_frame.place(x=0,y=280,width=810,height=250)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
     
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
     
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor_std)
        self.fetch_data()

        btnReset=Button(title,text="Exit",command=self.root.destroy,font=("arial",11,"bold"),width=15,bg="white",fg="red")
        btnReset.pack(side=RIGHT)
    # =============function declaration===================================
    def add_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                conn= pymysql.connect(host="admin",user="root",password="root",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                   
                                                                                                                                                                                                           
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo("Suceess",f"Student has been added...!!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # ==========fetch data===============
    def fetch_data(self):
        conn= pymysql.connect(host="localhost",user="admin",password="root",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ===========get cursor data=========
    def get_cursor_std(self,event=""):
        cursor_row_std=self.student_table.focus()
        content=self.student_table.item(cursor_row_std)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
      
    def std_update(self):
        if (self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()==""):
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Success","Are you sure you want  to update this Student",parent=self.root) 
                if update>0:
                    conn= pymysql.connect(host="localhost",user="root",password="root",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(

                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),                                                              
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_teacher.get(),   
                                                                                                                                                                self.va_std_id.get()
                                                                                                                            
                                                                                                                                                                 ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student successfully update completed....!!!",parent=self.root)                                                                                                                   
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()                                                                                                                                                                   
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def std_delete(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be reqaired",parent=self.root)
        else:
            emp_delete=messagebox.askyesno("Attendance Management System","Do you delete this student",parent=self.root)
            if emp_delete>0:
                conn= pymysql.connect(host="localhost",user="root",password="root",database="mydata")
                my_cursor=conn.cursor()
                sql="delete from student where student_id=%s"
                val=(self.va_std_id.get(),)
                my_cursor.execute(sql,val)
            else:
                if not emp_delete:
                    return 
        
            conn.commit()
            conn.close()
            self.fetch_data()
            self.clear() 

    def clear(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
      

    def search_data(self):
        if self.serchTxt_var.get()=="" or self.serch_var.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn= pymysql.connect(host='localhost',user='root',password='root',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'") 
                rows=my_cursor.fetchall() 

                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                
    
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # images function
    def openImg_1(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG File",".jpg"),("PNG File",".png"),("JPEG File",".jpeg"),("ALL File",".*")))
        img=Image.open(fln)
        img_left=img.resize((500,160),Image.Resampling.LANCZOS)
        self.im1=ImageTk.PhotoImage(img_left)
        self.f_lbl_1.config(image=self.im1)

    def openImg_2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG File",".jpg"),("PNG File",".png"),("JPEG File",".jpeg"),("ALL File",".*")))
        img=Image.open(fln)
        img_left=img.resize((500,160),Image.Resampling.LANCZOS)
        self.im2=ImageTk.PhotoImage(img_left)
        self.f_lbl_2.config(image=self.im2)

    def openImg_3(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG File",".jpg"),("PNG File",".png"),("JPEG File",".jpeg"),("ALL File",".*")))
        img=Image.open(fln)
        img_left=img.resize((550,160),Image.Resampling.LANCZOS)
        self.im3=ImageTk.PhotoImage(img_left)
        self.f_lbl_3.config(image=self.im3)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()