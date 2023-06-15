# Chameleon Challenge - Steganography - Easy - Points: 3
Created by: Ibrahim Selek

## Description
Chameleon Challenge is a Steganography-based Capture the Flag (CTF) challenge designed to test participants' skills in uncovering hidden information within image files. In this challenge, participants are presented with a image file. The objective is to detect and extract the hidden text or file. Participants must meticulously examine the image file, paying attention to pixel-level details, metadata, and employing steganography tools to reveal the concealed information. By successfully decoding the hidden secret, they are asked to submit this message, if it's correct participants will reveal the flag.  

## Deployment
This challenge is includes Frontend, Backend and Docker.

Frontend:
HTML,
CSS,
JavaScript

Backend:
Python/Flask

Deployment tool:
Docker,
Docker-Compose

The website is build with HTML, CSS and JavaScript. The backend is a Flask application. Flask is used for the back-end. Because it's used for the main-website and it uses python as programming language. There is no database created for this challenge. 

Docker is used for the deployment. The website and CTF have their own containers. So there are 2 containers, for this CTF. The Flask container is on port 5013. To run the containers, Docker-Compose is used for composing the containers and applying the settings to the containers.

The challenge can be accessed after loggging into the website and going to the CTF page. There you select Chameleon-Challenge.
Otherwise you can access it by this url: {ip/url}:5013/ctf/chameleon-challenge. By changing the port to 5013 and searching for /ctf/chameleon-challenge you will get to the challenge page.

## Solution
To solve this challenge, carefully analyze the image. Open the file provided and examine it closely. Check the file's metadata, metadata can often contain hidden messages or clues. Use appropriate (online)tools or software to extract and inspect the metadata thoroughly. Try steganography tools, utilize steganography tools and techniques to aid in uncovering the hidden text or file. Online tools, software applications, or scripts specifically designed for steganography can help reveal any concealed information within the file.

Try different steganography methods: Experiment with different steganography methods and algorithms. This may include techniques like LSB (Least Significant Bit) manipulation, hiding data in the frequency domain, or using encryption to encode and hide information. 
### First how to solve
Participants have to download the image file. (There are more than one! It will be downloaded randomly.) Than participants need to use steganography tools to find the hidden message in the file. It might be in the metadata or a hidden text file. 

### Techniques used to solve the challenge
Participants can use online tools or software to extract hidden message. Even they can write their on scripts. Just be aware, images you download uses different steganography techniques. **Attention** A solution worked for a image might not work for the others. 
Example online tools;
[Tool-1](https://stylesuxx.github.io/steganography/)
[Tool-2](https://futureboy.us/stegano/decinput.html)

### Flag location
If participants able to resolve the hidden message from the downloaded image, they need to submit it on the challenge page if it's correct the page will reload and the flag will appear.
