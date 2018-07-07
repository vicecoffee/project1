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
    return

@app.route("/login")
def login():
    return

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