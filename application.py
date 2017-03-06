
from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session
from sqllibrary import SQL
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
import random


app = Flask(__name__)

db = SQL("sqlite:///libmngsys.db")

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if session.get("user_id") is not None:
        return redirect(url_for("bookIssues"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':

        # ensure username is submitted
        if not request.form.get("username"):
            return render_template("apology.html", failMessage="must provide username")

        # ensure username does not exists in the database
        rows = db.execute("SELECT username FROM librarians_table")
        listOfUsernames = [ d['username'] for d in rows]
        if request.form.get("username") in listOfUsernames:
            return render_template("apology.html", failMessage="username already exists")

        # ensure password is submitted
        if not request.form.get("password"):
            return render_template("apology.html", failMessage="must provide password")

        # ensure password(Again) is submitted
        if not request.form.get("confirmPassword"):
            return render_template("apology.html", failMessage="must provide password(Again)")

        # ensure password and passwordConfirm Match
        if not (request.form.get("password") == request.form.get("confirmPassword")):
            return render_template("apology.html", failMessage="passwords don't match")

        rows = db.execute("INSERT INTO librarians_table (username, hash) VALUES (:username, :hashh)",
                    username=request.form.get("username"),
                    hashh=str(request.form.get("password")))
                    # hashh=pwd_context.hash(str(request.form.get("password"))))

        #login
        session["user_id"] = rows

        return redirect(url_for("bookIssues"))
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("apology.html", failMessage="must provide username")

        if not request.form.get("password"):
            return render_template("apology.html", failMessage="must provide password")

        rows = db.execute("SELECT * FROM librarians_table WHERE username = :username", username=request.form.get("username"))

        if len(rows) != 1 or (request.form.get("password") != rows[0]["hash"]):
            return render_template("apology.html", failMessage="invalid username and/or password")

        session["user_id"] = rows[0]["user_id"]

        return redirect(url_for("bookAvailable"))
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/members", methods=["GET", "POST"])
def member():
    # if not logged in
    if session.get("user_id") is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        if not request.form.get('member_name'):
            return render_template("apology.html", failMessage="Must Provide Member Name.")

        rows = db.execute("INSERT INTO member_table (member_name, branch, year_of_join) "
                            "VALUES (:mname, :branch, :yrj)",
                        mname=request.form.get("member_name"),
                        branch=request.form.get("branch"),
                        yrj=request.form.get("year_of_join"))

        rows = db.execute("SELECT * FROM member_table")
        return render_template("member.html", members=rows)
    else:
        rows = db.execute("SELECT * FROM member_table")
        return render_template("member.html", members=rows)


@app.route("/books", methods=["GET", "POST"])
def bookAvailable():
    """ Available Books. """
    # if not logged in
    if session.get("user_id") is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        if not request.form.get('book_name'):
            return render_template("apology.html", failMessage="Must Provide Book Name.")

        db.execute("INSERT INTO book_table (book_name, author, publication, subject, no_of_copies) "
                            "VALUES (:bname, :author, :pub, :sub, :noc)",
                    bname=request.form.get("book_name"),
                    author=request.form.get("author"),
                    pub=request.form.get("publication"),
                    sub=request.form.get("subject"),
                    noc=request.form.get("no_of_copies"))

        rows = db.execute("SELECT * FROM book_table")
        return render_template("bookAvailable.html" , books=rows)
    else:
        rows = db.execute("SELECT * FROM book_table")
        # return str(rows)
        return render_template("bookAvailable.html" , books=rows)


@app.route("/issues", methods=["GET", "POST"])
def bookIssues():
    # if not logged in
    if session.get("user_id") is None:
        return redirect(url_for("login"))

    if request.method == "POST":
        if not (request.form.get('book_id') or request.form.get('member_id') or request.form.get('issue_date') or request.form.get('return_date')):
            return render_template("apology.html", failMessage="Must Fullfil the form.")

        db.execute("INSERT INTO book_issue_table (book_id, member_id, issue_date, return_date) "
                            "VALUES (:bid, :mid, :idate, :rdate)",
                    bid=request.form.get("book_id"),
                    mid=request.form.get("member_id"),
                    idate=request.form.get("issue_date"),
                    rdate=request.form.get("return_date"))



        rows = db.execute("""
            SELECT book_issue_table.book_id, book_table.book_name, book_issue_table.member_id, member_table.member_name, issue_date, return_date
            FROM book_issue_table
            LEFT JOIN book_table
            ON book_issue_table.book_id = book_table.book_id
            LEFT JOIN member_table
            ON book_issue_table.member_id = member_table.member_id;

        """)
        return render_template("bookIssued.html" , issues=rows)

    else:
        rows = db.execute("""
            SELECT book_issue_table.book_id, book_table.book_name, book_issue_table.member_id, member_table.member_name, issue_date, return_date
            FROM book_issue_table
            LEFT JOIN book_table
            ON book_issue_table.book_id = book_table.book_id
            LEFT JOIN member_table
            ON book_issue_table.member_id = member_table.member_id;

        """)
        return render_template("bookIssued.html" , issues=rows)

