-- DROP DATABASE sql1;
-- CREATE DATABASE sql1;
-- CREATE USER 'sql1'@'%' IDENTIFIED BY 'Hello@CTF546!';



-- SQL challange sql1
USE sql1;

CREATE TABLE sql1.user (
	id INT NOT NULL AUTO_INCREMENT,
    name varchar(255),
    password varchar(255),
    primary key (id)
);

GRANT SELECT ON sql1.user TO 'sql1'@'%';

INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Abbey','dirt');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Addie','company');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Adele','letmein');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Adolph','sql2009');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Albert','change');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Alexys','testing');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Alfonzo','testing123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Alia','admin');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Allen','winter2013');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Amber','Password1!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Amelia','goat');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'root','root');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Amparo','98');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Anais','administator');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Anastasia','password123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Angus','alpine');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Annamarie','sa');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Arlie','Mar/11');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Ashley','secret123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Audie','wicked');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Axel','test-sql3');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Betty','qa');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Braulio','microsoft');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Braxton','default');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Breana','sqlpassword');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Britney','Summer2012');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Brock','P@55w0rd');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Bryana','welcome2');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Caitlyn','secret12');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Candelario','earth');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Carey','P@ssw0rd');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Carli','P@55w0rd!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Carmine','secret');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Chandler','burp');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Charlotte','login');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Chase','guessme');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Christelle','Password2');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Ciara','Password12');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Cierra','network');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Clarissa','winter2008');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Claud','Herfst123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Cleveland','winter2012');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Constantin','secret1212');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Corene','company1!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Cristal','sql2003');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Daren','football');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Dario','sasa');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Darrick','nt');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Darrion','Winter2012');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Dayton','P@ssw0rd!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Dedrick','test');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Della','master');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Deshawn','summer2012');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Dexter','bird');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Dixie','abc');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Earl','dragon');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Earnest','sql2008');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Edward','Sqlserver');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Effie','sqlaccount');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Elenora','company1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Elisa','sqlpass');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Elmer','complex');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Elta','sql2010');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Elvie','someday');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Emanuel','secuirty3');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Emelia','password');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Emmitt','Summer2009');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Erick','password12');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Esther','test');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Eve','password2');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Fay','sqlsqlsqlsql');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Felton','111111');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Filiberto','complexpassword');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Gabriella','1qaz2wsx');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Genevieve','2003');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Geoffrey','testsql');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Germaine','solo');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Grover','SqlServer');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Hadley','qwertyuiop');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Hailee','abcd123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Haleigh','unknown');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Harmony','summer2009');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Henry','sqlserver2005');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Holden','trust');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Hope','account');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Hortense','testtest');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Ibrahim','complex3');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Ilene','princess');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jacklyn','summer2011');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jaeden','P@ssw0rd!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jamel','95');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jamir','security');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jane','sql');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Javier','xp');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jayde','goat');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jeanette','summer2013');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jessy','summer2010');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jewel','sqlserver');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jonas','sqlsql');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jonathon','adminadmin');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Jordy','security3');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Julio','P@ssw0rd');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Junior','sasa');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kaitlyn','winter2011');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kaleigh','sql2011');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kaycee','testing');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kelley','123456');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kian','unchanged');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kim','Summer2008');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kole','complex2');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kris','winter2010');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Kyra','P@55w0rd!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Lacey','Welcome1212');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Leonor','winter2009');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'admin','CyberCTF{That#was@easy!right?}');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Leopoldo','P@ssword!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Leora','networks');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Libby','sql2000');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Lillie','sa');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Lonnie','microsoft');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Lorna','sqlpass123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Lucie','pass');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Lucy','private');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Mac','Winter2010');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Makenzie','sysadmin');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Marcel','networking');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Marcelina','SQLSQLSQLSQL');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Marcellus','sqlserver');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Mariano','2008');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Marie','sql2005');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Marilie','secret!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Maybelle','sqlserver2000');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Meggie','changeme');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Melyna','Password1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Miguel','Summer2013');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Milo','password1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Missouri','air');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Nicholas','Summer2011');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Nikita','starwars');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Noah','Passsql12');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Nola','P@55w0rd!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Norberto','god');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Nyasia','hugs');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Ona','test');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Orlo','Password1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Palma','secret1!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Paris','welcome');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Peyton','security1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Pink','changelater');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Providenci','monkey');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Raina','complex1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Randy','Summer2010');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Raven','Winter2008');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Renee','sqlsqlsqlsqlsql');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Rhoda','rain');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Rickey','Welcome123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Robb','admins');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Rosalia','basketball');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Rosalind','vista');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Rosie','summer2008');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Rubye','company!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Sadye','qwerty');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Sage','Welcome1234');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Sandrine','database');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Santiago','sqlsvr');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Scot','password!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Shannon','fire');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Sheila','baseball');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Stephen','welcome1');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Tiffany','bankbank');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Trinity','sql');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Tyrese','company123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Tyson','Winter2013');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Urban','abc123');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Vicky','12345678');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Victor','Winter2009');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Wilfred','Password!');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Willa','dev');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Zackary','water');
INSERT INTO sql1.user(id,name,password) VALUES (NULL,'Zula','snow');


