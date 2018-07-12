import os

from flask import Flask, session, request, render_template, redirect, jsonify
from flask_session import Session
from tempfile import mkdtemp
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, weather, get_comment, time, commanumber, decimalpercent
import json

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Custom filter
app.jinja_env.filters["time"] = time
app.jinja_env.filters["commanumber"] = commanumber
app.jinja_env.filters["decimalpercent"] = decimalpercent

@app.route("/")
def index():
    return render_template("index.html")

# Added the json dumps here to re-format the weather into a string
@app.route("/api/<string:zipcode>")
def api(zipcode):
    return jsonify(get_zipcode_weather(zipcode))


def get_zipcode_weather(zipcode):
    # Pull info from Darksky insert in HTML
    row = db.execute("SELECT locations.*, COUNT(user_id) as checkin_count FROM locations LEFT JOIN checkins on locations.loc_id=checkins.loc_id WHERE zipcode=:zipcode GROUP by locations.loc_id",
          {"zipcode": zipcode}).fetchone()
    return{
        "loc_id": row["loc_id"],
        "place_name": row["town"],
        "state": row["state"],
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "zip": row["zipcode"],
        "population": row["population"],
        "check_ins": row["checkin_count"],
        "weather":weather(row["latitude"], row["longitude"]),
        "comments":get_comment(row["zipcode"])
    }


@app.route("/location/<string:zipcode>", methods=["GET", "POST"])
@login_required
def location(zipcode):
    loc_dict = get_zipcode_weather(zipcode)
    # User reached route via POST
    if request.method == "POST":
        # I thought about making checkin a boolean and abstracting it away.  It could then disable the button in the html
        # much easier.  I didn't have time.
        rows = db.execute("SELECT * FROM checkins WHERE user_id = :user_id AND loc_id=:loc_id",
               {"user_id":session["user_id"], "loc_id":loc_dict["loc_id"]}).fetchall()
        if len(rows) >= 1:
            return apology("Sorry:  One checkin per user.", 400)
        db.execute("INSERT INTO checkins (user_id, loc_id, comment) VALUES (:user_id, :loc_id, :comment)",
                  { "user_id":session["user_id"], "loc_id":loc_dict["loc_id"], "comment":(request.form.get("comment"))})
        db.commit()
        return redirect("/location/{}".format(zipcode))

    if request.method == "GET":
        # Pull info from location table insert in HTML
        # Pull info from Darksky insert in HTML
        loc_dict = get_zipcode_weather(zipcode)
        return render_template("location.html",location_dict = get_zipcode_weather(zipcode))


# I copied this from CS50 Spring 2018 pset 7
@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("user_name"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        row = db.execute("SELECT * FROM users WHERE user_name = :user_name", {"user_name":request.form.get("user_name")}).fetchall()

        # Ensure username exists and password is correct
        if len(row) != 1:
            return apology("No such username or password.  Please register", 403)

        if not check_password_hash(row[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = row[0]["user_id"]
        print(session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# I copied this from CS50 Spring 2018 pset 7
@app.route("/logout")
def logout():
    # From pset7 of CS50
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# I copied this from CS50 Spring 2018 pset 7
@app.route("/register", methods=["GET", "POST"])
def register():
    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("user_name"):
            return apology("must provide username", 400)

        rows = db.execute("SELECT * FROM users WHERE user_name = :user_name", {"user_name":request.form.get("user_name")}).fetchall()

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
        db.execute("INSERT INTO users (user_name, real_name, hash) VALUES (:user_name, :real_name, :hashword)",
                   {"user_name":request.form.get("user_name"), "real_name":request.form.get("real_name"),
                   "hashword":generate_password_hash(request.form.get("password"))})
        db.commit()
        # Get user info for new user
        rows = db.execute("SELECT * FROM users WHERE user_name = :user_name", {"user_name":request.form.get("user_name")}).fetchall()

        # Log in user automatically.  Store id in session
        session["user_id"] = rows[0]["user_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/search_results")
@login_required
def search():
    fuzzy_input = "%{}%".format(request.args.get("search_input"))
    rows = db.execute("SELECT * FROM locations WHERE UPPER(town) like UPPER(:search_input) OR zipcode like :search_input LIMIT 30",
           {"search_input":fuzzy_input}).fetchall()
    if len(rows) < 1:
        return apology("Sorry. We don't have information on towns with populations smaller than 15,000")
    search_results_list =[]
    for row in rows:
        town = row["town"]
        state = row["state"]
        zipcode = row["zipcode"]
        town_state = {"town" :town, "state" :state, "zipcode" :zipcode}
        search_results_list.append(town_state)

    return render_template("search_results.html", list=search_results_list)

