from flask import Flask,render_template,url_for,session,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta
app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 

#database structure
class  users(db.Model):
    _tablename_= "user_detials"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(400),nullable=False)
    password = db.Column(db.String(1000),nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    birth_date = db.Column(db.String(20),nullable=False)
    email =db.Column(db.String(1000),nullable=False,unique=True)
    date_added= db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method =="POST":
        username = request.form.get("username")
        email = request.form.get("email")
        gender = request.form.get("gender")
        birth_date = request.form.get("date")
        passcode = request.form.get("password")

        new_user = users (
            username = username,
            email = email,
            gender = gender,
            birth_date = birth_date,
            password =passcode,
            date_added = datetime.now()
        )
        db.session.add(new_user) 
        db.session.commit()
    add = " <h1 color:green> success full registration </h1>"
    return add

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)