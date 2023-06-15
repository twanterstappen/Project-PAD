# Cracking the Meta - Crytographic Failures - Medium Level - 2

Created by: Ibrahim Selek

## Description
Cracking the Meta challenge is a Capture The Flag (CTF) challenge that focuses on the security vulnerabilities associated with file upload functionality and file analyse. Participants will be provided with a web application running on a local development server. Their goal is to exploit a file upload flaw to gain access to the website's sensetive file directory. After this they need to analyze the files on that directory to uncover the flag. 

## Deployment
This challenge is includes Frontend, Backend and Docker.
Frontend:
HTML,
CSS,
JavaScript

Backend:
Python/Flask
Database

Deployment tool:
Docker,
Docker-Compose

The website is build with HTML, CSS and JavaScript. The backend is a Flask application. Flask is used for the back-end. Because it's used for the main-website and it uses python as programming language. There is a database created for this challenge. Database keeps registered user's data.
Docker is used for the deployment. The website and CTF have their own containers. So there are 2 containers, for this CTF. The Flask container is on port 5013. To run the containers, Docker-Compose is used for composing the containers and applying the settings to the containers.
The challenge can be accessed after loggging into the website and going to the CTF page. There you select Cracking the META.

Otherwise you can access it by this url: {ip/url}:5005/ctf/crack-meta. By changing the port to 5005 and searching for /ctf/crack-meta you will get to the challenge page.

## Solution
To solve this challenge; 
First participants  have to register an account. 
Second register, participants can login with their username and password.
Third they have to upload a .txt file.
Fourth after uploading file they will be redirect to the website's directory
Fifth participants can download the file/files to examine
* The flag is hidden metadata(author section) of the file. 
### First how to solve
Participants can search for file upload flaw vulnerabilities. Then they have to upload a file with right extension. After reaching the directory they have to examine the files carefully. 
### Techniques used to solve the challenge
[Read](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload)
### Flag location
The flag is hidden in a image file's metadata as author.
