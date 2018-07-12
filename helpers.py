# Borrowed from pset7
import csv
import os
import urllib.request
import requests, json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#from time import strftime, localtime

from flask import redirect, render_template, request, session
from functools import wraps

# Set up database.  I didn't want to do this but I ended up with my get_comments function in this folder so I had to.
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# I copied this from CS50 Spring 2018 pset 7
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

# I copied this from CS50 Spring 2018 pset 7
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def make_darksky_url(latitude, longitude):
    """Query Darksky for weather at location based on latitiude & longitude and reutrn JSON"""
    # https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3
    # Set API request variables
    api_url_base = 'https://api.darksky.net/forecast'
    api_key = '9c102d141a42e76829cf376926f239db'
    # Headers
    content_type = 'application/json'

    specialstuff = "{}/{}/{},{}".format(api_url_base, api_key, latitude, longitude)
    print (specialstuff)
    return specialstuff

# I took away json.dumps so it could be an object to punch it into get_zipcode_weather in application.py  Where I
# turned around and put it back into json
def weather(latitude, longtiude):
    api_url = make_darksky_url(latitude, longtiude)
    local_weather = requests.get(api_url).json()
    return (local_weather["currently"])

# This was harder than it needed to be...but it works.
def get_comment(zipcode):
    comment_list = []
    rows = db.execute("SELECT checkins.comment FROM checkins INNER JOIN locations ON checkins.loc_id=locations.loc_id WHERE zipcode=:zipcode AND LENGTH(comment) > 0",
           {"zipcode": zipcode}).fetchall()
    if len(rows) == 0:
        words = "Nothing yet!"
        comment_list.append(words)
    else:
        for row in rows:
            words = row["comment"]
            comment_list.append(words)
    return comment_list

# I commented on this in the html...but I just ran out of time on this function.
# Changes the DarkSky epoch time to regular time
# https://docs.python.org/3/library/time.html
#def time(value):
    #strftime("%a, %d %b %Y %H:%M %Z", localtime(value))

#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-35.php
def commanumber(value):
    return ("{:,}".format(value))

#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
def decimalpercent(value):
    return ("{:.0%}".format(value))





