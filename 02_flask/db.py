from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#connection with database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_db'
db = SQLAlchemy(app)



class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    message=db.Column(db.String(120), nullable=False)
    # date=db.Column(db.String(120),date=datetime.now(), nullable=False)
    # def __repr__(self):
    #     return '<Contact %r>' % self.name
    
@app.route("/", methods=['GET','POST'])
def home():
      return render_template("index.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        phone=request.form.get('phone')
        
        email=request.form.get('email')
        message=request.form.get('message')
        entry = Contact(name=name,phone= phone,email=email,message=message);
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")

app.run(debug=True)