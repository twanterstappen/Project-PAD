# Emperor of roman - Crytographic Failures - Easy Level - 2

Created by: Ibrahim Selek

## Description

The Caesar Cipher is a very simple and common encryption method. It forms part of the basis of cryptography. 
It simply shifts a string of letters a certain number of positions up or down the alphabet. By solving this challenge you can gain 2 points. This challenge will help you to understand Crytographic Failrues. 

To access to challenge;

1. You need to register first. 
2. Login by your crediantels
3. Nagivate the challenge page. 
4. Choose the _Emperor of Roman_ challenge. Good luck!

## Deployment

This challenge is includes Frontend, Backend, Docker. 

Frontend:

_HTML,
CSS,
JavaScript_

Backend:

_Python/Flask_

Deployment tool:

_Docker,
Docker-Compose_

The website is build with HTML, CSS and JavaScript. The backend is a Flask application. Flask is used for the backend because it's used for the main-website and it uses python as language. There is no database created for this challenge. Docker is used for the deployment. 

The website and CTF have their own containers. So there are 2 containers, for this CTF. The Flask container is on port 5004 and the database is on port 3307. To run the containers, Docker-Compose is used for composing the containers and applying the settings to the containers.

The challenge can be accessed after loggging into the website and going to the CTF page. There you select Emperor of roman.
Otherwise you can access it by this url: {ip/url}:5004/ctf/roman-empire.
By changing the port to 5004 and searching for /ctf/roman-empire you will get to the challenge

## Solution

There are many approaches to cracking Caesar ciphers, but usually the best way to solve them is to write a script or run the string through a website which will print out all the possible shifts of a string. From those results the most comprehensible and logical solution can be chosen. [Try this link!] (https://cryptii.com/pipes/caesar-cipher)

### First how to solve
    Player should visit a website or write a script to solve the message with Caesar cipher. They need to simply shifts a string of letters a certain number of positions up or down the alphabet.
### Techniques used to solve the challenge
    Caeser cipher [Learn more!](https://en.wikipedia.org/wiki/Caesar_cipher)
### Flag location
    Flag is located in the secret message. 
