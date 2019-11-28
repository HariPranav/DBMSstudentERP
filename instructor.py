
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




#creating the instructor table with dept_id as primary key

## mycursor.execute(" create table instructor(dept_id varchar(10) primary key,instr_id varchar(10),rating varchar(10),qualification varchar(10), int(10))")

#creating the instructor table with dept_id as primary key and the dept_id as foreign key

## mycursor.execute("create table instructor (dept_id varchar(10) primary key,dept_id varchar(10) ,foreign key(dept_id) references instructor(dept_id) on delete cascade,rating varchar(10),qualification int(10))")


#creating table instructor with dept_id as foreign key and instr_id as primary key

## mycursor.execute("create table instructor(dept_id varchar(10) ,foreign key (dept_id) references instructor(dept_id) on delete cascade,instr_id varchar(10) primary key,rating int(10),qualification varchar(10))")

# create table courses with crc_id as primary_key and instr_id as foreign key

## mycursor.execute("create table courses (crc_id varchar(10) primary key,instr_id varchar(10), foreign key(instr_id) references instructor(instr_id),std_count bigint(10))")


#create table student with std_id as primary key , crc_id and dept_id as foreign keys

##mycursor.execute("create table student(std_id varchar(10) primary key,crc_id varchar(10),foreign key(crc_id) references courses(crc_id),dept_id varchar(10) , foreign key (dept_id) references instructor(dept_id),marks1 int(100),marks2 int(100),marks3 int(100),final_marks int (100))")


#mycursor.execute("Create table addresses(first_name text,last_name text,address text , city text , qualification text , zipcode int)")


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
    instr_id_label=instr_id.get()
    rating_label=rating.get()
    qualification_label=qualification.get()
    

    mycursor.execute("insert into instructor values('"+dept_id_label + "' , '"+instr_id_label + "' , '"+rating_label + "',  '"+qualification_label + "')")
    
    

    #clear the text boxes
    dept_id.delete(0,END)
    instr_id.delete(0,END)
    rating.delete(0,END)
    qualification.delete(0,END)
    
    
    

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
    mycursor.execute("delete from instructor  where dept_id='"+dept_id_label+"'")
   
    dept_id.delete(0,END)
    instr_id.delete(0,END)
    rating.delete(0,END)
    qualification.delete(0,END)
    
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
    instr_id_label=instr_id.get()
    rating_label=rating.get()
    qualification_label=qualification.get()
    
    
    mycursor.execute('''UPDATE instructor SET instr_id=%s ,rating =%s ,qualification =%s  where dept_id=%s''',(instr_id_label ,rating_label ,qualification_label ,dept_id_label) )
    # mycursor.execute("update instructor set instr_id_label='"+instr_id_label + "',rating_label='"+rating_label + "',qualification_label=  '"+qualification_label + "',_label='"+ _label + "' where dept_id_label='"+ dept_id_label +"'")
    
    dept_id.delete(0,END)
    instr_id.delete(0,END)
    rating.delete(0,END)
    qualification.delete(0,END)
    
    
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
    mycursor.execute("select * from instructor  where dept_id='"+dept_id_label+"'")
    rows = mycursor.fetchall()
    for row in rows:
        dept_id.insert(0,row[0])
        instr_id.insert(0,row[1])
        rating.insert(0,row[2])
        qualification.insert(0,row[3])
         
    
    
    mydb.commit()
    mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()
    mycursor.execute("select * from instructor")
    rows=mycursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = row[0]+ '      |      ' + row[1]  + '  |   '  + str(row[2]) +  '    |   '  + row[3]
        list.insert(list.size()+1 , insertData)

    mydb.commit()
    mydb.close()

dept_id=Entry(root,width=30)
dept_id.place(x=150,y=30)


instr_id=Entry(root,width=30)
instr_id.place(x=150,y=60)

rating=Entry(root,width=30)
rating.place(x=150,y=90)

qualification=Entry(root,width=30)
qualification.place(x=150,y=120)




# Create text box label for instructor table 

dept_id_label=Label(root , text="Department Id")
dept_id_label.place(x=20,y=30)


instr_id_label=Label(root , text="instr_id")
instr_id_label.place(x=20,y=60)

rating_label=Label(root , text="rating")
rating_label.place(x=20,y=90)

qualification_label=Label(root , text="qualification")
qualification_label.place(x=20,y=120)




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
