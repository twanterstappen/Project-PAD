from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session
import mysql.connector
import os


app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'

# Cryptocraphic Failure Easy
@app.route('/ctf/roman-empire', methods=['POST','GET'])
def romanempire():
    #Caesar cipher function
    def caesar_cipher(text, shift):
        result = ''
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
        return result
    # Caesar Cipher page/ctf
    encrypted_message = 'AilanknJank'
    if request.method == 'POST':
        decrypted_message = request.form['decrypted_message']
        if caesar_cipher(decrypted_message, 22) == 'AilanknJank':
            g.answer = 'Correct! Flag: CyberCTF{Say_my_name}'
            #return '<h1>Correct! Flag: CTF{Say_my_name}</h1>'
        else:
            g.answer = 'Incorrect'
            #return '<h1>Incorrect</h1>'
    return render_template('crypto1.html', encrypted_message=encrypted_message)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
