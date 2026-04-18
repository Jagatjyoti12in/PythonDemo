show databases;

create database nit;

show databases;

use nit;

create table student(
 name varchar(30),
 id int,
 age int not null primary key,
 adress varchar(50),
 mark int

)

desc student;

insert into student (marks,id,age,address,name) values(88,01,40,'Bhubaneswar','Jagat');


select * from student;


insert into student values('Rohit',02,30,'Bhybaneswar',78);

select * from student;

insert into student (marks,id,age,address,name) values (87,03,40,'Bhubaneswar','Amit');
insert into student (marks,id,age,address,name) values (90,04,40,'Bhubaneswar','Satyarth');
insert into student (marks,id,age,address,name) values (80,05,40,'Bhubaneswar','Rahul');  

select * from student;
show students;

select name from student;

select name,id from student;

select * from student where id=03;

insert into student (marks,id,age,address,name) values (85,06,32,'USA','Smith');

update student set name='Rohit Kumar' where id=02;

