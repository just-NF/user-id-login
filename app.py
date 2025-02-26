from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        mydb = mysql.connector.connect(
            host="sql8.freesqldatabase.com",
            user = "sql8764909",
            password = "8cEtjHmsu5",
            database = "sql8764909")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Passwrd = %s', (username, password))
        account = mycursor.fetchone()
        if account:
            print("Login is legit")
            name = account[1]
            id = account [0]
            msg = "login is legit babe"
            return render_template("login.html", msg=msg)
        else:
            msg="details ain't valid love,do it again"
            render_template("login.html", msg=msg)

        
@app.route("/register", methods=["POST", "GET"])
def register_user():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        mydb = mysql.connector.connect(
            host="sql8.freesqldatabase.com",
            user = "sql8764909",
            password = "8cEtjHmsu5",
            database = "sql8764909")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Passwrd = %s', (username, password))
        account = mycursor.fetchone()
        if account:
            msg ="Hey! We already have this account babe!"
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s,%s)', (username,password)) # new commend for sending information or creating a user
            mydb.commit()
            msg = "YOU REGISTERED BABE! "

    return render_template("registration.html", msg=msg)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("registration.html")

app.run(host="0.0.0.0", port=80, debug=True)