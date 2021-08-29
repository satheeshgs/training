import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Get input and validate submissions
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        message = ""

        if not name:
            message = "No name detected"
        elif not month:
            message = "Please enter valid month"
        elif not day:
            message  = "Please enter valid day"

        # TODO: Add the user's entry into the database
        # Only insert user into database if all values are entered
        else:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        birthdays = db.execute("SELECt * FROM birthdays")
        return render_template("index.html", message = message, birthdays = birthdays)

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays = birthdays)


