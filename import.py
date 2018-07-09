#to import csv files
import csv
from cs50 import SQL

db= SQL("postgres://vqhlwxbowulgoc:b44290dbb0843fe951312cf0dfa960092dd6c84ddf11dd105f0f01796e1cc688@ec2-23-23-220-19.compute-1.amazonaws.com:5432/d888fp495haud5")
f= open("zips.csv")
reader = csv.reader(f)
#
next(reader)
# I tested the import with a dummy command and it populated until 318. I deleted those entries.
for row in reader:
	db.execute("INSERT INTO locations (zipcode, town, state, latitude, longitude, population) VALUES (:zipcode, :town, :state, :latitude, :longitude, :population)", zipcode=row[0], town=row[1], state=row[2], latitude=row[3], longitude=row[4], population=row[5])