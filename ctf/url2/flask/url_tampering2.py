from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session
import os



app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'


id_names = {1:['9438 XX','admin','CyberCTF{collecting9the#waste}'], 2:['5126 MC','Gilze','6-12-2024'], 3:['1601 AP','Enkhuizen','8-7-2030'], 4:['7783 AM','Gramsbergen','7-6-2024'], 5:['3572 JC','Utrecht','5-12-2050'], 6:['5961 GM','Horst','4-3-2025'], 7:['2132 XE','Hoofddorp','6-9-2063'], 8:['8561 BD','Balk','7-8-2025'], 9:['2671 AL','Naaldwijk','3-2-2025'], 10:['4286 CE','Almkerk','4-6-2025']}


@app.route('/ctf/garbage4you')
def garbage():
    zip = request.args.get('zip')
    for id in id_names:
        if id_names[id][0] == zip:
            return redirect(f'/ctf/garbage4you/calendar?id={id}')
    if zip:
        flash('Wrong zip code', 'error')
    else:
        flash('Please login first', 'info')
    return render_template('login.html')

@app.route('/ctf/garbage4you/calendar')
def calendar():
    id_web = request.args.get('id')
    if id_web:
        for id in id_names:
            if str(id) == id_web:
                g.zip = id_names[id][0]
                g.city = id_names[id][1]
                g.date = id_names[id][2]
                return render_template('calendar.html')
            
    return redirect(url_for('garbage'))

@app.errorhandler(Exception)
def general(error):
    error_code = str(error)
    error_code = error_code[:3]
    if error_code == '404':
        g.path = request.path
        
    g.error = error
    return render_template("error/general.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
