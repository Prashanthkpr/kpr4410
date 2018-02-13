from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import  SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://'
db=SQLAlchemy(app)

@app.route('/')
@app.route('/user')
def index(user=None):
    return render_template('login.html',user=user)
app.run(debug=True)

@app.route("/login",methods=['POST'])
def login():
    username=str(request.form['name'])
    password = str(request.form['password'])
    cursor=db.cursor()
    cursor.excute('select name, password from login_bd where name="+username" and password="+password"')
    user=cursor.fetchone()
    if len(user)==1:
        return "Login is Successful"
    else:
        return "Login Failure"