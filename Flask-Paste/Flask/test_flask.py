from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('inicio.html')
@app.route('/Coding')
def code():
    return render_template('code.html')
@app.route('/Editing')
def editing():
    return render_template('editing.html')
@app.route('/Kontakt')
def kontakt():
    return render_template('kontakt.html')

app.run()