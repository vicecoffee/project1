# Borrowed from pset7
import csv
import os
import urllib.request
import requests, json
from time import localtime, asctime

from flask import redirect, render_template, request, session
from functools import wraps


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

# I took away json.dumps so it could be an object
def weather(latitude, longtiude):
    api_url = make_darksky_url(latitude, longtiude)
    local_weather = requests.get(api_url).json()
    return (local_weather["currently"])

# Changes the DarkSky epoch time to regular time
# https://docs.python.org/3/library/time.html
def time(value):
    return asctime(localtime(value))

#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-35.php
def commanumber(value):
    return ("{:,}".format(value))

#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
def decimalpercent(value):
    return ("{:.0%}".format(value))





