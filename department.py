
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




#creating the department table with dept_id as primary key

## mycursor.execute(" create table department(dept_id varchar(10) primary key,coll_id varchar(10),hod_id varchar(10),instr_count varchar(10), int(10))")

#creating the department table with dept_id as primary key and the dept_id as foreign key

## mycursor.execute("create table department (dept_id varchar(10) primary key,dept_id varchar(10) ,foreign key(dept_id) references department(dept_id) on delete cascade,hod_id varchar(10),instr_count int(10))")


#creating table instructor with dept_id as foreign key and instr_id as primary key

## mycursor.execute("create table instructor(dept_id varchar(10) ,foreign key (dept_id) references department(dept_id) on delete cascade,instr_id varchar(10) primary key,rating int(10),qualification varchar(10))")

# create table courses with crc_id as primary_key and instr_id as foreign key

## mycursor.execute("create table courses (crc_id varchar(10) primary key,instr_id varchar(10), foreign key(instr_id) references instructor(instr_id),std_count bigint(10))")


#create table student with std_id as primary key , crc_id and dept_id as foreign keys

##mycursor.execute("create table student(std_id varchar(10) primary key,crc_id varchar(10),foreign key(crc_id) references courses(crc_id),dept_id varchar(10) , foreign key (dept_id) references department(dept_id),marks1 int(100),marks2 int(100),marks3 int(100),final_marks int (100))")


#mycursor.execute("Create table addresses(first_name text,last_name text,address text , city text , instr_count text , zipcode int)")


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
    dept_id_label=dept_id.get()
    coll_id_label=coll_id.get()
    hod_id_label=hod_id.get()
    instr_count_label=instr_count.get()
    

    mycursor.execute("insert into department values('"+dept_id_label + "' , '"+coll_id_label + "' , '"+hod_id_label + "',  '"+instr_count_label + "')")
    
    

    #clear the text boxes
    dept_id.delete(0,END)
    coll_id.delete(0,END)
    hod_id.delete(0,END)
    instr_count.delete(0,END)
    
    
    

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
    dept_id_label=dept_id.get()
    mycursor.execute("delete from department  where dept_id='"+dept_id_label+"'")
   
    dept_id.delete(0,END)
    coll_id.delete(0,END)
    hod_id.delete(0,END)
    instr_count.delete(0,END)
    
    mydb.commit()
    MessageBox.showinfo("Deleted Status","Deleted Successfully")
    show()
    
    mydb.close()
    


def update():
    
     #insert into the table 
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #insert into the table 
    dept_id_label=dept_id.get()
    coll_id_label=coll_id.get()
    hod_id_label=hod_id.get()
    instr_count_label=instr_count.get()
    
    
    mycursor.execute('''UPDATE department SET coll_id=%s ,hod_id =%s ,instr_count =%s  where dept_id=%s''',(coll_id_label ,hod_id_label ,instr_count_label ,dept_id_label) )
    # mycursor.execute("update department set coll_id_label='"+coll_id_label + "',hod_id_label='"+hod_id_label + "',instr_count_label=  '"+instr_count_label + "',_label='"+ _label + "' where dept_id_label='"+ dept_id_label +"'")
    
    dept_id.delete(0,END)
    coll_id.delete(0,END)
    hod_id.delete(0,END)
    instr_count.delete(0,END)
    
    
    mydb.commit()
    MessageBox.showinfo("Update Status","Updated Successfully")
    show()
    mydb.close()
    

    #clear the text boxes
    


def get():
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #execute the query
    dept_id_label=dept_id.get()
    mycursor.execute("select * from department  where dept_id='"+dept_id_label+"'")
    rows = mycursor.fetchall()
    for row in rows:
        coll_id.insert(0,row[1])
        hod_id.insert(0,row[2])
        instr_count.insert(0,row[3])
         
    
    
    mydb.commit()
    mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()
    mycursor.execute("select * from department")
    rows=mycursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = row[0]+ '      |      ' + row[1]  + '  |   '  + row[2] +  '    |   '  + str(row[3])
        list.insert(list.size()+1 , insertData)

    mydb.commit()
    mydb.close()

dept_id=Entry(root,width=30)
dept_id.place(x=150,y=30)


coll_id=Entry(root,width=30)
coll_id.place(x=150,y=60)

hod_id=Entry(root,width=30)
hod_id.place(x=150,y=90)

instr_count=Entry(root,width=30)
instr_count.place(x=150,y=120)




# Create text box label for department table 

dept_id_label=Label(root , text="department Id")
dept_id_label.place(x=20,y=30)


coll_id_label=Label(root , text="coll_id")
coll_id_label.place(x=20,y=60)

hod_id_label=Label(root , text="hod_id")
hod_id_label.place(x=20,y=90)

instr_count_label=Label(root , text="instr_count")
instr_count_label.place(x=20,y=120)




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
