
from tkinter import *
import mysql.connector
import tkinter.messagebox as MessageBox

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")

print(mydb)

if(mydb):
    print("Connection successfull")

else:
    print("Connection unsuccessfull")

mycursor=mydb.cursor()


#creating the student table with std_id as primary key

## mycursor.execute(" create table student(std_id varchar(10) primary key,crc_id varchar(10),dept_id varchar(10),marks1 varchar(10),marks2 int(10))")

#creating the department table with dept_id as primary key and the std_id as foreign key

## mycursor.execute("create table department (dept_id varchar(10) primary key,std_id varchar(10) ,foreign key(std_id) references student(std_id) on delete cascade,hod_id varchar(10),instr_count int(10))")


#creating table instructor with dept_id as foreign key and instr_id as primary key

## mycursor.execute("create table instructor(dept_id varchar(10) ,foreign key (dept_id) references department(dept_id) on delete cascade,instr_id varchar(10) primary key,rating int(10),qualification varchar(10))")

# create table courses with crc_id as primary_key and instr_id as foreign key

## mycursor.execute("create table courses (crc_id varchar(10) primary key,instr_id varchar(10), foreign key(instr_id) references instructor(instr_id),std_count bigint(10))")


#create table student with std_id as primary key , crc_id and dept_id as foreign keys

##mycursor.execute("create table student(std_id varchar(10) primary key,crc_id varchar(10),foreign key(crc_id) references courses(crc_id),dept_id varchar(10) , foreign key (dept_id) references department(dept_id),marks1 int(100),marks2 int(100),marks3 int(100),final_marks int (100))")


#mycursor.execute("Create table addresses(first_name text,last_name text,address text , city text , marks1 text , zipcode int)")


mycursor.execute("show tables")
for db in mycursor: 
    print(db)




Tk, Label
root = Tk()
root.title('DBMS MINI PROJECT')
root.geometry("1000x1000")

# #create a submit function into the database 

def insert():

    #to add data into the database we need to also add the creation of the database part ito the function
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #insert into the table 
    std_id_label=std_id.get()
    crc_id_label=crc_id.get()
    dept_id_label=dept_id.get()
    marks1_label=marks1.get()
    marks2_label=marks2.get()
    marks3_label=marks3.get()
    final_marks_label=final_marks.get()

    mycursor.execute("insert into student values('"+std_id_label + "' , '"+crc_id_label + "' , '"+dept_id_label + "',  '"+marks1_label + "','"+ marks2_label + "','"+ marks3_label + "','"+ final_marks_label + "')")
    
    

    #clear the text boxes
    std_id.delete(0,END)
    crc_id.delete(0,END)
    dept_id.delete(0,END)
    marks1.delete(0,END)
    marks2.delete(0,END)
    marks3.delete(0,END)
    final_marks.delete(0,END)
    
    

    mydb.commit()
    MessageBox.showinfo("Inserted Status","Inserted Successfully")
    show()
    mydb.close()
    
#
def delete():

     #delete from the table 
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #execute the query
    std_id_label=std_id.get()
    mycursor.execute("delete from student  where std_id='"+std_id_label+"'")
   
    std_id.delete(0,END)
    crc_id.delete(0,END)
    dept_id.delete(0,END)
    marks1.delete(0,END)
    marks2.delete(0,END)
    marks3.delete(0,END)
    final_marks.delete(0,END)
    mydb.commit()
    MessageBox.showinfo("Deleted Status","Deleted Successfully")
    show()
    
    mydb.close()
    


def update():
    
     #insert into the table 
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #insert into the table 
    std_id_label=std_id.get()
    crc_id_label=crc_id.get()
    dept_id_label=dept_id.get()
    marks1_label=marks1.get()
    marks2_label=marks2.get()
    marks3_label=marks3.get()
    final_marks_label=final_marks.get()
    mycursor.execute('''UPDATE student SET crc_id=%s ,dept_id =%s ,marks1 =%s ,marks2=%s ,marks3=%s ,final_marks=%s where std_id=%s''',(crc_id_label ,dept_id_label ,marks1_label,marks2_label ,marks3_label ,final_marks_label ,std_id_label) )
    # mycursor.execute("update student set crc_id_label='"+crc_id_label + "',dept_id_label='"+dept_id_label + "',marks1_label=  '"+marks1_label + "',marks2_label='"+ marks2_label + "' where std_id_label='"+ std_id_label +"'")
    
    std_id.delete(0,END)
    crc_id.delete(0,END)
    dept_id.delete(0,END)
    marks1.delete(0,END)
    marks2.delete(0,END)
    marks3.delete(0,END)
    final_marks.delete(0,END)
    mydb.commit()
    MessageBox.showinfo("Update Status","Updated Successfully")
    show()
    mydb.close()
    

    #clear the text boxes
    


def get():
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #execute the query
    std_id_label=std_id.get()
    mycursor.execute("select * from student  where std_id='"+std_id_label+"'")
    rows = mycursor.fetchall()
    for row in rows:
        crc_id.insert(0,row[1])
        dept_id.insert(0,row[2])
        marks1.insert(0,row[3])
        marks2.insert(0,row[4])   
        marks3.insert(0,row[5])
        final_marks.insert(0,row[6])
    mydb.commit()
    mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()
    mycursor.execute("select * from student")
    rows=mycursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = row[0]+ '      |      ' + row[1]  + '  |   '  + row[2] +  '    |   '  + str(row[3]) +  '   |    '  + str(row[4]) +  '   |    '  + str(row[5])+  '   |    '  + str(row[6])
        list.insert(list.size()+1 , insertData)

    mydb.commit()
    mydb.close()

std_id=Entry(root,width=30)
std_id.place(x=150,y=30)


crc_id=Entry(root,width=30)
crc_id.place(x=150,y=60)

dept_id=Entry(root,width=30)
dept_id.place(x=150,y=90)

marks1=Entry(root,width=30)
marks1.place(x=150,y=120)

marks2=Entry(root,width=30)
marks2.place(x=150,y=150)

marks3=Entry(root,width=30)
marks3.place(x=150,y=180)


final_marks=Entry(root,width=30)
final_marks.place(x=150,y=210)


# Create text box label for student table 

std_id_label=Label(root , text="student Id")
std_id_label.place(x=20,y=30)


crc_id_label=Label(root , text="crc_id")
crc_id_label.place(x=20,y=60)

dept_id_label=Label(root , text="dept_id")
dept_id_label.place(x=20,y=90)

marks1_label=Label(root , text="marks1")
marks1_label.place(x=20,y=120)

marks2_label=Label(root , text="marks2")
marks2_label.place(x=20,y=150)

marks3_label=Label(root , text="marks3")
marks3_label.place(x=20,y=180)

final_marks_label=Label(root , text="finalMarks")
final_marks_label.place(x=20,y=210)


# # create a submit button







insert = Button(root , text="insert" , command=insert)
insert.place(x=50,y=250)

delete = Button(root , text="Delete " , command=delete)
delete.place(x=100,y=250)

update = Button(root , text="Update " , command=update)
update.place(x=160,y=250)

get = Button(root , text="get" , command=get)
get.place(x=220,y=250)

list = Listbox(root)
list.place(x=350 , y=20)
show()
root.mainloop()
