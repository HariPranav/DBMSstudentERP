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
use dbproject;
desc student;

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

insert into student(std_id,crc_id,dept_id,marks1,marks2,marks3) values("B001", "DAA","CS",50,60,50);
select * from student;
insert into student values("B002", "DS", "IS",60,70,80,100);
insert into student values("B003", "SE", "CV",50,60,70,100);
insert into student values("B004", "MP", "ME",50,60,70,100);
insert into student values("B005", "DMS", "ECE",50,60,70,100);

 
 show tables;
 
show databases;
create database dbproject;
use dbproject;

show tables;
desc addresses;
drop table addresses;
drop database dbproject;
select * from college;
select * from department;


create database libraryProg1;
use libraryProg1;
create  table book (book_id varchar(10) primary key , title varchar(10) , publisher_name varchar(10),publisher_year varchar(10));
create table book_author(book_id varchar(10),author_name varchar(10) , foreign key(book_id) references book(book_id) on delete cascade);
create table publisher(name varchar(10) primary key , address varchar(10) , phone varchar(10));
create table library_branch(branch_id varchar(10) primary key , branch_name varchar(10) , address varchar(10));
create table book_copies(book_id varchar(10), foreign key(book_id) references book(book_id) on delete cascade,  branch_id varchar(10),foreign key(branch_id) references library_branch(branch_id) on delete cascade,no_of_copies int(10));
create table book_lending(book_id varchar(10),foreign key (book_id) references book(book_id) on delete cascade,branch_id varchar(10) ,foreign key(branch_id) references library_branch(branch_id) on delete cascade,card_no varchar(10) primary key,date_out date,due_date date);
use  libraryProg1;
select  b.book_id , title  , publisher_name , publisher_year ,author_name , no_of_copies, l.branch_id from book b ,book_author,publisher,library_branch l,book_copies order by l.branch_id; 
select card_no ,count(*) as "no_of_" from book_lending where date_out between "2017-01-01" and "2018-01-01" ;
create view view1 as select b.book_id,title , c.branch_id ,no_of_copies from book b , library_branch c , book_copies ;
select * from view1;
create table book1 (book_id varchar(10) , title varchar(10) , publisher_name varchar(10),publisher_year varchar(10) , primary key(book_id,publisher_year)) , partision by RANGE(pub_year) (partision p0 values less than (2017),partision p1 values less than (2017) );




insert  into book values("001","hariP","hari","2018");
insert  into book values("002","fiftyp","hari","2019");
insert into book_author values("001","hari");
insert  into book_author values("002","Somraj");
insert  into publisher values("Arun","98876788","Cmrit");
insert  into publisher values("hari","98876438","Aecs");
insert into library_branch values("b001","Shant","Lib1");
insert into library_branch values("b002","Bant","Lib2");
insert into book_copies values("001","b001",10);
insert into book_copies values("002","b002",30);
insert into book_lending values("001","b001","1", "2018-10-11","2010-10-11");
insert into book_lending values("002","b002","4", "2017-10-11","2010-10-1");
use libraryprog1;






create database	orderProg2;
use orderProg2;
create table salesman(salesman_id varchar(10) primary key,name varchar(10),city varchar(10),commission varchar(10));
create table customer(cus_id varchar(10) primary key, cus_name varchar(10),city varchar(10),grade varchar(10),salesman_id varchar(10),foreign key(salesman_id) references salesman(salesman_id) on delete cascade);
create table orders(ord_no varchar(10),pur_amt varchar(10),ord_date date,cus_id varchar(10), foreign key(cus_id) references customer(cus_id) on delete cascade,salesman_id varchar(10) , foreign  key (salesman_id) references salesman(salesman_id) on delete cascade);
drop table customer;
drop table salesman;
use orderProg2;
insert into salesman values("001","harish","blore","50");
insert into salesman values("002","harh","mlore","20");
insert into customer values("001","hari","blore","10","001");
insert into customer values("002","Shyam","mlore","9","002");
insert into orders values("001","10000","2018-07-1","001","002");
insert into orders values("001","10000","2018-07-1","002","001");
use orderProg2;
select a.name,b.cus_id, b.salesman_id ,count(*) from salesman a, customer b where a.salesman_id=b.salesman_id  group by (a.salesman_id) having cus_id > 1;
select count(*),cus_name,avg(grade),city  from customer group by cus_name having avg(grade) > city="blore";

create database movieProg3;
create table actor(act_id varchar(10) primary key , act_name varchar(10), act_gender varchar(10));
create table director(dir_id varchar(10) primary key , dir_name varchar(10), dir_phone varchar(10));
create table movies( mov_id varchar(10) primary key , mov_title varchar(10), mov_year varchar(10),mov_lang varchar(10),dir_id varchar(10) ,foreign key(dir_id) references director(dir_id) on delete cascade);
create table movie_cast(act_id varchar(10 ) ,foreign key(act_id) references actor(act_id), mov_id varchar(10) , foreign key(mov_id) references movies(mov_id) on delete cascade, role varchar(10));
create table rating(mov_id varchar(10),foreign key (mov_id) references movies(mov_id) on delete cascade,review varchar(10),stars int(10));
drop table rating;
use  movieProg3;
select mov_title from movies a, director b where a.dir_id=b.dir_id and b.dir_name="gamit";
select m.mov_title , count(*) from movies m , movie_cast mc where m.mov_id = mc.mov_id and act_id in (select act_id from movie_cast group by act_id having count(*) > 1);
select mov_title from movies where mov_id in(select mov_id from movie_cast where act_id in(select act_id from movie_cast group by act_id having count(*)>1)); 
select act_name from actor a, join  movie_cast mc  on a.act_id=mc.act_id  join  movie_cast mc on mc.mov_id=m.mov_id  where m.mov_year not between 2000 and 2015;
update rating set stars=5 where mov_id in(select mov_id from movies where dir_id in(select dir_id from director where dir_name='gamit'));












insert into actor values("001","hari","M");
insert into actor values("002","gari","F");
insert into director values("001","gamit","788202");
insert into director values("002","amit","78820223");
insert into movies values ("001","desa","2019","eng","001");
insert into movies values ("002","desai","2018","hin","002");
insert into movie_cast values("001","001","barber");
insert into movie_cast values("002","002","karborber");
insert into rating values("001","good",5);
insert into rating values("002","good",3);









create database collegeProg4;
use collegeProg4;
create table student (usn varchar (10)primary key, address varchar(10),phone varchar(10),gender varchar(10));
create table semsec(ssid varchar(10) primary key,sem varchar(10),sec varchar(10));
create table class(usn varchar(10) , foreign key(usn) references student(usn),ssid varchar(10) , foreign key(ssid)  references	semsec(ssid) on delete cascade);
create table subjects(subcode varchar(10) primary key, title varchar(10) , sem varchar(10),credits varchar(10));
create table ia_marks(usn varchar(10) , foreign key(usn) references student(usn) on delete cascade,subcode varchar(10) references subjects(subcode) on delete cascade,ssid varchar(10) , foreign key(ssid) references semsec(ssid) on delete cascade , test1 int(50),test2 int(50),test3 int(50),final_ia int(100));




use dbproject;
DELIMITER //   
CREATE PROCEDURE allcolleges()
 BEGIN     SELECT *  FROM colleges;
 END //   DELIMITER ;
select * from college;

CALL allcollegesallcollegesallcollegesallcolleges;

# Creating trigger
use dbproject;
drop table student;
create trigger finalmarks before insert on student for each row set new.final_marks=((new.marks1 + new.marks2 +new.marks3)-least(new.marks1,new.marks2,new.marks3))/2;
 delimiter //
 
CREATE TRIGGER NegativeMarks BEFORE INSERT ON student FOR EACH ROW IF NEW.marks1 < 0 THEN SET NEW.marks1 = 0; END IF;//
delimiter ;

delimiter //
CREATE TRIGGER NegativeMarks1 BEFORE INSERT ON student FOR EACH ROW IF NEW.marks2 < 0 THEN SET NEW.marks2 = 0; END IF;//
delimiter ;


delimiter //
CREATE TRIGGER NegativeMarks2 BEFORE INSERT ON student FOR EACH ROW IF NEW.marks3 < 0 THEN SET NEW.marks3 = 0; END IF;//
delimiter ;




drop trigger finalmarks;
drop table student;
select * from student;





