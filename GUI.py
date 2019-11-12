
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


#creating the college table with coll_id as primary key

## mycursor.execute(" create table college(coll_id varchar(10) primary key,board varchar(10),accred varchar(10),state varchar(10),ranking int(10))")

#creating the department table with dept_id as primary key and the coll_id as foreign key

## mycursor.execute("create table department (dept_id varchar(10) primary key,coll_id varchar(10) ,foreign key(coll_id) references college(coll_id) on delete cascade,hod_id varchar(10),instr_count int(10))")


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
    coll_id_label=coll_id.get()
    board_label=board.get()
    accred_label=accred.get()
    state_label=state.get()
    ranking_label=ranking.get()

    mycursor.execute("insert into college values('"+coll_id_label + "' , '"+board_label + "' , '"+accred_label + "',  '"+state_label + "','"+ ranking_label + "')")
    
    

    #clear the text boxes
    coll_id.delete(0,END)
    board.delete(0,END)
    accred.delete(0,END)
    state.delete(0,END)
    ranking.delete(0,END)
    
    

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
    coll_id_label=coll_id.get()
    mycursor.execute("delete from college  where coll_id='"+coll_id_label+"'")
   
    coll_id.delete(0,END)
    board.delete(0,END)
    accred.delete(0,END)
    state.delete(0,END)
    ranking.delete(0,END)
    mydb.commit()
    MessageBox.showinfo("Deleted Status","Deleted Successfully")
    show()
    
    mydb.close()
    


def update():
    
     #insert into the table 
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #insert into the table 
    coll_id_label=coll_id.get()
    board_label=board.get()
    accred_label=accred.get()
    state_label=state.get()
    ranking_label=ranking.get()
    
    mycursor.execute('''UPDATE college SET board=%s ,accred =%s ,state =%s ,ranking=%s where coll_id=%s''',(board_label ,accred_label ,state_label,ranking_label ,coll_id_label) )
    # mycursor.execute("update college set board_label='"+board_label + "',accred_label='"+accred_label + "',state_label=  '"+state_label + "',ranking_label='"+ ranking_label + "' where coll_id_label='"+ coll_id_label +"'")
    
    coll_id.delete(0,END)
    board.delete(0,END)
    accred.delete(0,END)
    state.delete(0,END)
    ranking.delete(0,END)
    
    mydb.commit()
    MessageBox.showinfo("Update Status","Updated Successfully")
    show()
    mydb.close()
    

    #clear the text boxes
    


def get():
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()

    #execute the query
    coll_id_label=coll_id.get()
    mycursor.execute("select * from college  where coll_id='"+coll_id_label+"'")
    rows = mycursor.fetchall()
    for row in rows:
        board.insert(0,row[1])
        accred.insert(0,row[2])
        state.insert(0,row[3])
        ranking.insert(0,row[4])   
    
    
    mydb.commit()
    mydb.close()

def show():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")
    mycursor=mydb.cursor()
    mycursor.execute("select * from college")
    rows=mycursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = row[0]+ '      |      ' + row[1]  + '  |   '  + row[2] +  '    |   '  + row[3] +  '   |    '  + str(row[4])
        list.insert(list.size()+1 , insertData)

    mydb.commit()
    mydb.close()

coll_id=Entry(root,width=30)
coll_id.place(x=150,y=30)


board=Entry(root,width=30)
board.place(x=150,y=60)

accred=Entry(root,width=30)
accred.place(x=150,y=90)

state=Entry(root,width=30)
state.place(x=150,y=120)

ranking=Entry(root,width=30)
ranking.place(x=150,y=150)



# Create text box label for college table 

coll_id_label=Label(root , text="College Id")
coll_id_label.place(x=20,y=30)


board_label=Label(root , text="Board")
board_label.place(x=20,y=60)

accred_label=Label(root , text="Accredation")
accred_label.place(x=20,y=90)

state_label=Label(root , text="State")
state_label.place(x=20,y=120)

ranking_label=Label(root , text="Ranking")
ranking_label.place(x=20,y=150)


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
