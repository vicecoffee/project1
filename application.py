import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@login_required

@app.route("/")
def index():
    # TO SEARCH
    return "Project 1: TODO"

@app.route("/register")
def register():
    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username is unique
        if len(rows) >= 1:
            return apology("username already exists", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password and confirmation match
        if request.form.get("confirmation") != request.form.get("password"):
            return apology("must match password and confirm", 400)

        # Insert username into db
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hashword)",
                   username=request.form.get("username"), hashword=generate_password_hash(request.form.get("password")))

        # Get user info for new user
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Log in user automatically.  Store id in session
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/login")
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    # From pset7 of CS50
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/location", methods=["GET", "POST"])
def location():
    # User reached route via POST
    if request.method == "POST":
        # Same as "GET: table for location info & darksky BUT disable FORMS
        # Write SQL commands to add checkin to db
        return render_template("location.html")

    if request.method == "GET":
        # TO DISPLAY INFO & FORMS
        # Pull info from location table insert in HTML
        # Don't forget to make a form for checkin
        # Pull info from Darksky insert in HTML
        return render_template("location.html")