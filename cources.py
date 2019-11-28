
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


#creating the courses table with crc_id as primary key

## mycursor.execute(" create table courses(crc_id varchar(10) primary key,instr_id varchar(10),std_count varchar(10),state varchar(10),ranking int(10))")

#creating the department table with dept_id as primary key and the crc_id as foreign key

## mycursor.execute("create table department (dept_id varchar(10) primary key,crc_id varchar(10) ,foreign key(crc_id) references courses(crc_id) on delete cascade,hod_id varchar(10),instr_count int(10))")


#creating table instructor with dept_id as foreign key and instr_id as primary key

## mycursor.execute("create table instructor(dept_id varchar(10) ,foreign key (dept_id) references department(dept_id) on delete cascade,instr_id varchar(10) primary key,rating int(10),qualification varchar(10))")

# create table courses with crc_id as primary_key and instr_id as foreign key

## mycursor.execute("create table courses (crc_id varchar(10) primary key,instr_id varchar(10), foreign key(instr_id) references instructor(instr_id),std_count bigint(10))")


#create table student with std_id as primary key , crc_id and dept_id as foreign keys

##mycursor.execute("create table student(std_id varchar(10) primary key,crc_id varchar(10),foreign key(crc_id) references courses(crc_id),dept_id varchar(10) , foreign key (dept_id) references department(dept_id),marks1 int(100),marks2 int(100),marks3 int(100),final_marks int (100))")


#mycursor.execute("Create table addresses(first_name text,last_name text,address text , city text , state text , zipcode int)")


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
    crc_id_label=crc_id.get()
    instr_id_label=instr_id.get()
    std_count_label=std_count.get()
    

    mycursor.execute("insert into courses values('"+crc_id_label + "' , '"+instr_id_label + "' , '"+std_count_label + "')")
    
    

    #clear the text boxes
    crc_id.delete(0,END)
    instr_id.delete(0,END)
    std_count.delete(0,END)
    
    
    

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
    crc_id_label=crc_id.get()
    mycursor.execute("delete from courses  where crc_id='"+crc_id_label+"'")
   
    crc_id.delete(0,END)
    instr_id.delete(0,END)
    std_count.delete(0,END)
    
    mydb.commit()
    MessageBox.showinfo("Deleted Status","Deleted Successfully")
    show()
    
    mydb.close()
    


def update():
    
     #insert into the table 
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #insert into the table 
    crc_id_label=crc_id.get()
    instr_id_label=instr_id.get()
    std_count_label=std_count.get()
    
    
    mycursor.execute('''UPDATE courses SET instr_id=%s ,std_count =%s where crc_id=%s''',(instr_id_label ,std_count_label ,crc_id_label) )
    # mycursor.execute("update courses set instr_id_label='"+instr_id_label + "',std_count_label='"+std_count_label + "',state_label=  '"+state_label + "',ranking_label='"+ ranking_label + "' where crc_id_label='"+ crc_id_label +"'")
    
    crc_id.delete(0,END)
    instr_id.delete(0,END)
    std_count.delete(0,END)
    
    
    mydb.commit()
    MessageBox.showinfo("Update Status","Updated Successfully")
    show()
    mydb.close()
    

    #clear the text boxes
    


def get():
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #execute the query
    crc_id_label=crc_id.get()
    mycursor.execute("select * from courses  where crc_id='"+crc_id_label+"'")
    rows = mycursor.fetchall()
    for row in rows:
        instr_id.insert(0,row[1])
        std_count.insert(0,row[2])
         
    
    
    mydb.commit()
    mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()
    mycursor.execute("select * from courses")
    rows=mycursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = row[0]+ '      |      ' + row[1]  + '  |   '  + str(row[2])
        list.insert(list.size()+1 , insertData)

    mydb.commit()
    mydb.close()

crc_id=Entry(root,width=30)
crc_id.place(x=150,y=30)


instr_id=Entry(root,width=30)
instr_id.place(x=150,y=60)

std_count=Entry(root,width=30)
std_count.place(x=150,y=90)





# Create text box label for courses table 

crc_id_label=Label(root , text="Cource Id")
crc_id_label.place(x=20,y=30)


instr_id_label=Label(root , text="Instructor_id")
instr_id_label.place(x=20,y=60)

std_count_label=Label(root , text="student_count")
std_count_label.place(x=20,y=90)




# # create a submit button







insert = Button(root , text="insert" , command=insert)
insert.place(x=50,y=180)

delete = Button(root , text="Delete " , command=delete)
delete.place(x=100,y=180)

update = Button(root , text="Update " , command=update)
update.place(x=160,y=180)

get = Button(root , text="get" , command=get)
get.place(x=220,y=180)

list = Listbox(root)
list.place(x=350 , y=20)
show()
root.mainloop()
