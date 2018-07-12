#to import csv files
import csv
from cs50 import SQL

db= SQL("postgres://vqhlwxbowulgoc:b44290dbb0843fe951312cf0dfa960092dd6c84ddf11dd105f0f01796e1cc688@ec2-23-23-220-19.compute-1.amazonaws.com:5432/d888fp495haud5")
f= open("zips.csv")
reader = csv.reader(f)
#
next(reader)
# I tested it many times.  The primary key is very high. Also, added "0" for zipcodes that started with "0".
for row in reader:
    zipcode= "{:05}".format(int(row[0]))
    db.execute("INSERT INTO locations (zipcode, town, state, latitude, longitude, population) VALUES (:zipcode, :town, :state, :latitude, :longitude, :population)", zipcode=zipcode, town=row[1], state=row[2], latitude=row[3], longitude=row[4], population=row[5])