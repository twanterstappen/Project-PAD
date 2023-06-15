from flask import Flask, render_template, request, send_file, redirect, url_for, flash, Blueprint, request, g, session
import random
import os
import base64

app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'

# Route to challenge page
@app.route('/ctf/chameleon-challenge')
def index():
    return render_template('steganography.html')


#Route for the download a random photo
@app.route('/download_image')
def download_image():
    downloads_dir = os.path.join(app.root_path, 'static', 'downloads')
    photo_files = os.listdir(downloads_dir)
    random_photo = random.choice(photo_files)
    photo_path = os.path.join(downloads_dir, random_photo)
    return send_file(photo_path, as_attachment=True)


# To check if the hidden message is matches
@app.route('/check_message', methods=['POST'])
def check_message():
    hidden_message = request.form['message']

    # Compare the hidden message with the correct answer
    correct_answer = 'Chameleons are experts in the art of hiding.'
    if hidden_message.strip().lower() == correct_answer.lower():
        flag = 'CyberCTF{Ch@m3l30n_0f_$t3n06r@phy}'
        g.answer = f'Congratulations! Your flag is {flag}.'
        #result = 'Congratulations! You completed the challenge.'
    else:
        g.answer = 'Sorry, your answer is incorrect.'
        #result = 'Sorry, your answer is incorrect.'

    return render_template('steganography.html', )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
