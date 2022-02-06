from flask import flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app= flask(_name_)
#connect to the database
app.config ['SQLALCHEMY_DATABASE_URI']='postgresql://DB_USER:PASSWORD@HOST/DATABASE'
db = SQLAlchemy(app)
# Define db model
class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(120))
def __init__(self,email, username):
        self.email = email
        self.username = username

@app.route("/", methods=['POST'])
def hello():
    return render_template("checkout.html")
ef thankyou():
    if request.method == "POST":
        email = request.form["emailAddress"]
        username = request.form["username"]
        print(request.form)
        #last step: commit
    data = Data(email,username)
    db.session.add(data)
    db.session.commit() #execute
    return render_template('thankyou.html')

    if _name_ == "_main_":
        app.debug=True
        app.run()
