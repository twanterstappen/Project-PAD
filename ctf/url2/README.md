# Garbage4you - URL tampering - medium - 5
Created by: Twan Terstappen

## Description

In this challenge you will need to change the url to get the flag. With this you can are tampering the URL



## Deployment

This CTF is build with html and flask only, because when u are going to solve the challenege u only have to navigate to the right directory. Also the CTF has an apart docker container running in the background.




## Solution


### First how to solve
To solve the challenge u first need to login with a zip code
after that you need to change the url to this: {ip}:5011/ctf/garbage4you/calendar?id=1
Or
visit this: /ctf/garbage4you/calendar?id=1
### Techniques used to solve the challenge
Changing the id to 1
### Flag location
U can find the flag in the id=1 page of the admin