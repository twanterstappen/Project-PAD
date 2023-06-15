# WordPress - SQL Injection - Medium - Points: 7
Created by: Twan Terstappen

## Description

The challenge is an intermediate SQL injection. You get to a default WordPress page. To get to the login form, you need to navigate to /wp-admin. WordPress is a web content management system. To gain access, you need to inject a SQL statement and return the credentials from one of the admin. With those credentials you can login into the WordPress site to reveal the flag.

With this injection, you get to know a advaced technique of SQL Injection.

For solving this challenge you will receive 7 points. This challenge is hard and for someone that is has some knowledge of SQL injection it's challenging. [Learn about the basic and more advanced SQL injections](https://vm-thijs.ewi.utwente.nl/ctf/sql)

The challenge can be accessed after logging into the website and going to the CTF page. There you select WordPress. 
Otherwise you can access it by this url: {ip/url}:5003/ctf/wordpress. 
By changing the port to 5003 and searching for /ctf/wordpress you will get to the challenge page


## Deployment

What is the deployment. Frontend, Backend, database, docker.
For every technique create a sub title
- Frontend:
    - HTML
    - CSS
    - JavaScript

- Backend:
    - Flask

- Database:
    - MariaDB

- Deployment tool:
    - Docker
    - Docker-Compose

The website is build with HTML, CSS and JavaScript. The backend is a Flask application that connects to a database. Flask is used for the backend because it's used for the main-website and it uses python as language. MariaDB is used as database because it's lighweight compared to MySQL and there is only a small database needed. Docker is used for the deployment. The website and database have their own containers. So there are 2 containers, for this CTF. The Flask container is on port 5003 and the database is on port 3310. To run the containers, Docker-Compose is used for composing the containers and applying the settings to the containers.



## Solution

 

### First how to solve
You can use this injection:
```
'; SELECT table_name FROM information_schema.tables #Here you can see all the tables where you have access to
```
After that:
```
'; SELECT * from superuser #retrieve all the superuser credentials
```
Now you can login with one of the superusers credentials.

### Techniques used to solve the challenge
advanced SQL Injection, break out of a string, closing the first statement and beginning a new one, get information from information_schema.tables,
retrieve all the data from the right table.

### Flag location
Flag is located after loggin in as one of the superusers