from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    naam = "Amar Nath Prajapati"
    return render_template('index.html',name=naam)

@app.route("/contact")
def contact():
    pata = "Jaunpur U.P."
    return render_template('contact.html',address=pata)

app.run(debug=True)