# phpMyAdmin - SQL Injection - Easy - Points: 3
Created by: Twan Terstappen

## Description

The challenge is a beginners SQL injection. You get the login form for phpMyAdmin. phpMyAdmin is a free opensource administration tool for MySQL and MariaDB. To gain access you need to injected a sql statement and return all the data. 
By gainging access you can find the flag in the returned data that is displayed after logging in.

With this challenge you use a basic type of injection. With this you got a good foundation to complete the next level and try a more complex SQL Injection.

For this challenge you will receive 3 points. This challenge is easy to understand and for someone that is new to SQL injection is easy to understand after some research. [Learn about basic SQL injection](https://www.w3schools.com/sql/sql_injection.asp)

The challenge can be accessed after loggging into the website and going to the CTF page. There you select phpMyAdmin. 
Otherwise you can access it by this url: {ip/url}:5001/ctf/phpmyadmin. 
By changing the port to 5001 and searching for /ctf/phpmyadmin, you will get to the challenge page.


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

The website is build with HTML, CSS and JavaScript. The backend is a Flask application that connects to a database. Flask is used for the backend because it's used for the main-website and it uses python as language. MariaDB is used as database because it's lighweight compared to MySQL and there is only a small database needed. Docker is used for the deployment. The website and database have their own containers. So there are 2 containers, for this CTF. The Flask container is on port 5001 and the database is on port 3308. To run the containers, Docker-Compose is used for composing the containers and applying the settings to the containers.



## Solution

 

### First how to solve
You can use one of these injections:
```
' OR 1=1 -- #Gets all the data and search for the user: admin
```
```
' OR name='admin' -- #Gets only the user admin with the flag
```
### Techniques used to solve the challenge
Basic SQL Injection, break out of a string, applying an always true Boolean and commenting the remainding syntax out.
### Flag location
Flag is located as password of user: admin