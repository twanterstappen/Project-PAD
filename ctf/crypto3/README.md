# Hunting in the woods - Cryptographic Failure - Hard - Points: 8
Created by: Antonyo Jarouj

## Description
This challenge is going about a private key who was leaked from a website, it is up to you to find the private key and enter the website (get the flag ) using the python code and the file flag.txt
When I was making the challenge I have learned a lot of things about cryptography that I did not knew, like how to encrypt en decrypt messages and why is it important to decrypt or to encrypt a message and the logic behind cryptography. And ofcourse there are a lot of things that I do not know yet, so I am going to improve myself to get better and better.

## Deployment
There is a lot of technique that was used by creating this CTF. This CTF has actually a private container running on it self, there was also tools like python and flask used to make the backend of the ctf, if u want to check the CTF out, u can visit it by entering ctf/passwordhunt in the url. The front-end tools that we have used to make this CTF are Html and css, just a basic tools. The front end of the CTF looks very similar of the front end of the home page, because we prefer to focus on one theme.

## Solution
### First how to solve
First thing that u have to do to solve this challange is to download the python file. When u have downloaded the file u have to work in the terminal and make sure to navigate to the directory where the python file is on your system.

### Techniques used to solve the challenge
U have now to do the following:
> python ende.py -d flag.txt .
The program is asking u for a private key, u can find the encrypted version of the key in the robots.txt file;
password = a2V5OjE5ZDM3bnJyODkybXhmYTk4M2xvMHBxOTJiY2Y0NzMy
U have to decrypt this value using tool like cyberchef for example and then u will get the private key: 19d37nrr892mxfa983lo0pq92bcf4732
When u fill the private key and hit the enter button u wil get the flag.

### Flag location
U can find the flag when u decrypt the flag.txt file using the correct password
