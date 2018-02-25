drop database documentFinder;
create database documentFinder;

use documentFinder;


drop table user_search_history;
 create table user_search_history(feeback_id Int(11) auto_increment primary key,
application_id varchar(100), search_text varchar(1000), url_provided varchar(500),  users_feedback varchar(100),
 search_date timestamp default current_timestamp);

 drop table url_details;
 create table url_details(url_id Int(11) auto_increment primary key, url_name varchar(100), url_application varchar(100), url_desc varchar(100), url_title varchar(100),
created_date timestamp default current_timestamp, url_application_id int(11));

ALTER TABLE url_details ADD CONSTRAINT app_id_fk
FOREIGN KEY (url_application_id) REFERENCES application_details (application_id);


insert into url_details values(1,"https://www.facebook.com","opera","social network","FACEBOOK PAGE",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'), 1);
insert into url_details values(2,"https://www.google.com","dal","search engine","GOOGLE PAGE",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'), 2);
insert into url_details values(3,"https://www.youtube.com","cfodl","videos","YOUTUBE PAGE",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'), 3);
insert into url_details values(4,"https://www.superdatascience.com","home","professional","SUPERDATASCIENCE PAGE",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'), 4);
insert into url_details values(5,"https://www.linkedin.com","opera","social network","LINKEDIN PAGE",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'), 1);
commit;

drop table application_details;
create table application_details(application_id int(11) auto_increment primary key,  application_name varchar(100), application_base_url varchar(500), added_date timestamp default current_timestamp);

insert into application_details values(1, "opera", "https://odyssey.com/opera",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'));
insert into application_details values(2, "dal", "https://odyssey.com/dal",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'));
insert into application_details values(3, "cfodl", "https://odyssey.com/cfodl",STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'));
insert into application_details values(4, "home", "https://odyssey.com/home", STR_TO_DATE('18-FEB-2018', '%d-%M-%Y'));
commit;



select * from url_details;
select * from application_details;
select * from user_search_history;
