# Project 1

Web Programming with Python and JavaScript

!.  Application.py
    a. @app.route("/") -Basic landing page
    b. @app.route("/api/<string:zipcode>")
        -def api(zipcode) - constructs the API url request
        -def get_zipcode_weather(zipcode) - Creates the dict which more location.html is based
    c. @app.route("/location/<string:zipcode>", methods=["GET", "POST"])
        -def location(zipcode)- Fills in locations.html and updates comments table
    d. @app.route("/login", methods=["GET", "POST"])- login function with some validation
    e. @app.route("/logout")
    f. @app.route("/register", methods=["GET", "POST"])- register function with some validation
    g. @app.route("/search_results")
        -def search()- Searches locations table using like and Upper to increase chances of correct item

2. Helpers.py
    a. def apology(message, code=400) - returns message for user about input errors
    b. def login_required(f)- makes sure the user is logged in when searching & checking in
    c. def make_darksky_url(latitude, longitude)- makes the darksjy url
    d. def weather(latitude, longtiude)-helps make part of the darksky url
    e. def get_comment(zipcode)- gets the comments for a location
    f. def commanumber(value)- filter to clean up the population value from location table
    g. def decimalpercent(value)- filter to clean up the humidity value from the weather json

3.  import.py - function to import csv location info to db
4.  requirements.txt
5.  zips.csv
6.  apology.html
7.  index.html- General Homepage-extends layout
8.  layout.html- Main html document
9.  location.html- Page with information on locations, weather, and checkins-extends layout
10.  register.html-extends layout
11.  search_results.html-List results for search queries-extends layout
12.  css.css- Basic CSS

