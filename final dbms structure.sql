 create table college(coll_id varchar(10) primary key,
 board varchar(10),
 accred varchar(10),
 state varchar(10),
 ranking int(10));

 create table department (dept_id varchar(10) primary key,
 coll_id varchar(10) ,
 foreign key(coll_id) references college(coll_id) on delete cascade,
 hod_id varchar(10),
 instr_count int(10)
 );
 
 
 create table instructor(dept_id varchar(10) ,
 foreign key (dept_id) references department(dept_id) on delete cascade,
 instr_id varchar(10) primary key,
 rating int(10),
 qualification varchar(10));
 
 create table courses (crc_id varchar(10) primary key,
 instr_id varchar(10), foreign key(instr_id) references instructor(instr_id),
 std_count bigint(10)
 );
 
 create table student(std_id varchar(10) primary key,
 crc_id varchar(10),foreign key(crc_id) references courses(crc_id),
 dept_id varchar(10) , foreign key (dept_id) references department(dept_id),
 marks1 int(100),
 marks2 int(100),
 marks3 int(100),
 final_marks int (100)
 );
--  
 insert into college values("CR" , "VTU" , "A+" , "KARNATAKA" , 56);
 insert into college values("RA" , "VTU" , "A++" , "KARNATAKA" , 2);
insert into college values("RV" , "VTU" , "A++++" , "KARNATAKA" , 1);
insert into college values("BMS" , "VTU" , "A+++" , "KARNATAKA" , 2);
insert into college values("REV" , "University" , "V+" , "KARNATAKA" , 100);

insert into department values("CS","CR", "H1",50);
insert into department values("IS","RA",  "H2",30);
insert into department values("CV","RV",  "H3",40);
insert into department values("ME", "BMS", "H4",60);
insert into department values("ECE","REV",  "H5",40);

insert into instructor values("CS", "H1" , 8 , "BE");
insert into instructor values("IS", "H1" , 8 , "BE");
insert into instructor values("CV", "H1" , 8 , "BE");
insert into instructor values("ME", "H1" , 8 , "BE");
insert into instructor values("ECE", "H1" , 8 , "BE");

insert into courses values("DAA", "H1" ,100);
insert into courses values("DS", "H1" ,100);
insert into courses values("SE", "H1" ,100);
insert into courses values("MP", "H1" ,100);
insert into courses values("DMS", "H1" ,100);

insert into student values("B001", "DAA","CS", 50,60,70,100);
insert into student values("B002", "DS", "IS",60,70,80,100);
insert into student values("B003", "SE", "CV",50,60,70,100);
insert into student values("B004", "MP", "ME",50,60,70,100);
insert into student values("B005", "DMS", "ECE",50,60,70,100);
