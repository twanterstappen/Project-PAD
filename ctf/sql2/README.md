# Vaccine4you - SQL Injection - Medium - Points: 5
Created by: Twan Terstappen

## Description

The challenge is a beginners/intermediate SQL injection. You get to the login form for Vaccine4you. Vaccine4you is a website where users can login and see what vaccine they get. To gain access, you need to inject a SQL statement and return the password from the admin. 
By retrieving the data, you can decode the password with Base64.

With this injection, you get to know a more in-depth SQL Injection.

For solving this challenge you will receive 5 points. This challenge is easy to understand and for someone that is new to SQL injection is easy to understand after some research. [Learn about the basic and more advanced SQL injections](https://vm-thijs.ewi.utwente.nl/ctf/sql)

The challenge can be accessed after logging into the website and going to the CTF page. There you select Vaccine4you. 
Otherwise you can access it by this url: {ip/url}:5002/ctf/vaccine4you. 
By changing the port to 5002 and searching for /ctf/vaccine4you you will get to the challenge page


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

The website is build with HTML, CSS and JavaScript. The backend is a Flask application that connects to a database. Flask is used for the backend because it's used for the main-website and it uses python as language. MariaDB is used as database because it's lighweight compared to MySQL and there is only a small database needed. Docker is used for the deployment. The website and database have their own containers. So there are 2 containers, for this CTF. The Flask container is on port 5002 and the database is on port 3309. To run the containers, Docker-Compose is used for composing the containers and applying the settings to the containers.



## Solution

 

### First how to solve
You can use this injection:
```
'; SELECT password FROM user -- #Gets the first entry of the database, by "accident" is that the admin
```
After that, the string that you get has to be decoded. You can use [Cyberchef base64 decoder](https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true))

### Techniques used to solve the challenge
advanced SQL Injection, break out of a string, closing the first statement and beginning a new one, select the right column from the right table and commenting the remainding syntax out.

### Flag location
Flag encoded with base64 and is located as password of user: admin