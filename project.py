from tkinter import*
from tkinter import ttk
import pymysql
class studentsinfo:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1550x950')
        self.root.title('NTH')
        title1=Label(self.root,text='Welcome to NTH students information',font=('cooper black',40,'bold'),bg='orange',fg='black')
        title1.pack(fill='x')
        
        self.rollnoVar=StringVar()
        self.fristnameVar=StringVar()
        self.lastnameVar=StringVar()
        self.emailidVar=StringVar()
        self.contactVar=StringVar()
        self.courseVar=StringVar()
        self.locationVar=StringVar()

        DataEntryFrame=Frame(self.root,bg='blue')
        DataEntryFrame.place(x=5,y=70,width=500,height=900)
        DataDisplayFrame=Frame(self.root,bg='blue')
        DataDisplayFrame.place(x=510,y=70,width=1050,height=700)
        #WORK WITH FRAMES
        title2=Label(DataEntryFrame,text='Data Entry Here....',font=('cooper black',20,'bold'),bg='red',fg='white')
        title2.grid(row=0,columnspan=2,padx=100,pady=20)
        #ROLL NO
        rnoLable=Label(DataEntryFrame,text='ROLL NO:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        rnoLable.grid(row=1,column=0,sticky='w')

        rnoentry=Entry(DataEntryFrame,textvariable=self.rollnoVar,font=('Book Antiqua',20,'bold'))
        rnoentry.grid(row=1,column=1,sticky='E',pady=10)
        #CREATE FRIST NAME
        FnameLabel=Label(DataEntryFrame,text='FRIST NAME:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        FnameLabel.grid(row=2,column=0,sticky='w')

        Fnameentry=Entry(DataEntryFrame,textvariable=self.fristnameVar,font=('Book Antiqua',20,'bold'))
        Fnameentry.grid(row=2,column=1,sticky='E',pady=10)
        #CREATE LAST NAME
        LnameLabel=Label(DataEntryFrame,text='LAST NAME:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        LnameLabel.grid(row=3,column=0,sticky='w')

        Lnameentry=Entry(DataEntryFrame,textvariable=self.lastnameVar,font=('Book Antiqua',20,'bold'))
        Lnameentry.grid(row=3,column=1,sticky='E',pady=13)
        #EMAIL ID
        EidLabel=Label(DataEntryFrame,text='EMAIL ID:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        EidLabel.grid(row=4,column=0,sticky='w')

        Eidentry=Entry(DataEntryFrame,textvariable=self.emailidVar,font=('Book Antiqua',20,'bold'))
        Eidentry.grid(row=4,column=1,sticky='E',pady=13)
        #CONTACT NUMBER
        CnoLabel=Label(DataEntryFrame,text='CONTACT NO:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        CnoLabel.grid(row=5,column=0,sticky='w')

        Cnoentry=Entry(DataEntryFrame,textvariable=self.contactVar,font=('Book Antiqua',20,'bold'))
        Cnoentry.grid(row=5,column=1,sticky='E',pady=13)
        #COURSE
        CLabel=Label(DataEntryFrame,text='COURSE:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        CLabel.grid(row=6,column=0,sticky='w')

        Centry=Entry(DataEntryFrame,textvariable=self.courseVar,font=('Book Antiqua',20,'bold'))
        Centry.grid(row=6,column=1,sticky='E',pady=13)

        
        #LOCATION
        LocLabel=Label(DataEntryFrame,text='LOCATION:',font=('Book Antiqua',15,'bold'),bg='green',fg='white')
        LocLabel.grid(row=7,column=0,sticky='w')

        Locentry=Entry(DataEntryFrame,textvariable=self.locationVar,font=('Book Antiqua',20,'bold'))
        Locentry.grid(row=7,column=1,sticky='E',pady=13)
        #CREATINGLABLES FOR BUTTONS
        btnFrame=Frame(DataEntryFrame,bg='red',border=4,relief=RAISED)
        btnFrame.place(x=10,y=500,width=480,height=100)
        #ADD BUTTON
        addbtn=Button(btnFrame,text='ADD',command=self.adding,font=('Book Antiqua',12,'bold'),bg='orange',fg='black')
        addbtn.grid(row=0,column=1,pady=40,padx=20)
        #UPDATE BUTTON
        Updatebtn=Button(btnFrame,text='UPDATE',command=self.updating,font=('Book Antiqua',12,'bold'),bg='orange',fg='black')
        Updatebtn.grid(row=0,column=2,pady=40,padx=20)
        
        #CLEAR BUTTON
        Clearbtn=Button(btnFrame,text='CLEAR',command=self.clearning,font=('Book Antiqua',12,'bold'),bg='orange',fg='black')
        Clearbtn.grid(row=0,column=3,pady=40,padx=20)
        #DELET BUTTON
        Deletebtn=Button(btnFrame,text='DELETE',command=self.deleting,font=('Book Antiqua',12,'bold'),bg='orange',fg='black')
        Deletebtn.grid(row=0,column=4,pady=20,padx=20)
        #creating Data Display frame
        title3=Label(DataDisplayFrame,text='Data Display Here',font=('cooper black',20,'bold'),bg='red',fg='white')
        title3.grid(padx=300,pady=20)

        tableframe=Frame(DataDisplayFrame,border=3,bg='red',relief=RAISED)
        tableframe.place(x=10,y=85,width=835,height=510)

        self.StudentsData=ttk.Treeview(tableframe,columns=('roll_no','frist_name','last_name','emailid','contactno','course','location'))
        self.StudentsData.heading('roll_no',text='Roll No')
        self.StudentsData.heading('frist_name',text='Frist Name')
        self.StudentsData.heading('last_name',text='Last Name')
        self.StudentsData.heading('emailid',text='Email Id')
        self.StudentsData.heading('contactno',text='CONTACT NO')
        self.StudentsData.heading('course',text='COURSE')
        self.StudentsData.heading('location',text='LOCATION')

        self.StudentsData['show']='headings'

        self.StudentsData.column('roll_no',width=50,anchor='center')
        self.StudentsData.column('frist_name',width=120,anchor='center')
        self.StudentsData.column('last_name',width=110,anchor='center')
        self.StudentsData.column('emailid',width=150,anchor='center')
        self.StudentsData.column('contactno',width=130,anchor='center')
        self.StudentsData.column('course',width=130,anchor='center')
        self.StudentsData.column('location',width=130,anchor='center')

        self.StudentsData.pack()
        self.fetching()
        self.StudentsData.bind("<ButtonRelease-1>",self.get_cursor)

    def adding(self):
        connection=pymysql.connect(host='localhost',user='root',password='venkey@123',db='studentsinfo')
        c=connection.cursor()
        c.execute('insert into studentsdata values(%s,%s,%s,%s,%s,%s,%s)',
                  (
                    self.rollnoVar.get(),
                    self.fristnameVar.get(),
                    self.lastnameVar.get(),
                    self.emailidVar.get(),
                    self.contactVar.get(),
                    self.courseVar.get(),
                    self.locationVar.get(),
                    ))


        connection.commit()
        self.clearning()
        connection.close()
    def clearning(self):
        self.rollnoVar.set(''),
        self.fristnameVar.set(''),
        self.lastnameVar.set(''),
        self.emailidVar.set(''),
        self.contactVar.set(''),
        self.courseVar.set(''),
        self.locationVar.set(''),
    def fetching(self):
        connection=pymysql.connect(host='localhost',user='root',password='venkey@123',db='studentsinfo')
        c=connection.cursor()
        c.execute('select * from studentsdata')
        data=c.fetchall()
        self.StudentsData.delete(*self.StudentsData.get_children())
        for i in data:
            self.StudentsData.insert('',END,value=i)
        connection.commit()
        connection.close()
    def get_cursor(self,Var):
        cursor_row=self.StudentsData.focus()
        content=self.StudentsData.item(cursor_row)
        row=content['values']
        self.rollnoVar.set(row[0])
        self.fristnameVar.set(row[1])
        self.lastnameVar.set(row[2])
        self.emailidVar.set(row[3])
        self.contactVar.set(row[4])
        self.courseVar.set(row[5])
        self.locationVar.set(row[6])
    def updating(self):
        connection=pymysql.connect(host='localhost',user='root',password='venkey@123',db='studentsinfo')
        c=connection.cursor()
        c.execute('update StudentsData set fristname=%s,lastname=%s,emailid=%s,contactno=%s,course=%s,location=%s where id=%s',
                  (
                      self.fristnameVar.get(),
                      self.lastnameVar.get(),
                      self.emailidVar.get(),
                      self.contactVar.get(),
                      self.courseVar.get(),
                      self.locationVar.get(),
                      self.rollnoVar.get()
                      ))
        connection.commit()
        self.fetching()
        self.clearning()
        connection.close()
    def deleting(self):
        connection=pymysql.connect(host='localhost',user='root',password='venkey@123',db='studentsinfo')
        c=connection.cursor()
        c.execute('delete from StudentsData where id=%s',self.rollnoVar.get())
        connection.commit()
        self.fetching()
        self.clearning()
        connection.close()
        
        

                
root=Tk()
obj=studentsinfo(root)


