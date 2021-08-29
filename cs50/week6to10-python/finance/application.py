import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    name = db.execute("SELECT username FROM users where id = ?", user_id)
    user_cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])

    # Get the stocks he owns from the stocks table
    stocks = db.execute(
        "SELECT symbol, name_stock as name, SUM(num) as shares, price, SUM(total) as total FROM stocks WHERE userid = ? GROUP BY symbol HAVING SUM(num) > 0", user_id)
    print(stocks)
    total_cash_stocks = 0

    for stock in stocks:
        total_cash_stocks = total_cash_stocks + stock["total"]

    total_cash = total_cash_stocks + user_cash

    # Pass details to index.html to render for loading
    return render_template("index.html", name=name, stocks=stocks, user_cash=user_cash, total_cash=total_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Get the quote price of the share and the number of shares to buy
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        try:
            shares = int(shares)
            if shares < 0:
                return apology("must provide positive number of shares", 400)
        except ValueError:
            return apology("shares must be a positive integer", 400)

        cost = 0

        if symbol == None:
            return apology("must provide symbol to buy", 400)
        else:
            try:
                price = lookup(symbol)
            except:
                return apology("Invalid price returned", 400)

        # Calculate cost price of the shares
        try:
            cost = price["price"]*int(shares)
        except:
            return apology("price not found", 400)

        try:
            stock = (lookup(request.form.get("symbol")))["name"]
        except:
            return apology("symbol error", 400)

        # Check if user has sufficient balance
        user_id = session["user_id"]
        print(user_id)
        user_cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])
        print(user_cash)
        print(cost)

        if user_cash < cost:
            return apology("You do not have sufficient cash", 403)
        # If user has sufficient balance, then execute the transaction and update user's balance
        else:
            # Calculate the user cash
            user_cash = user_cash - cost
            print(user_cash)
            # Insert into user's database, the cash
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash, user_id)
            # Insert into the stocks database about who purchased what
            db.execute("INSERT INTO stocks (userid, symbol, name_stock, num, price, type, total) VALUES (?,?,?,?,?,?,?)",
                       user_id, symbol.lower(), stock, int(shares), price["price"], "buy", cost)

            # Return to index
            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    history = db.execute(
        "SELECT date, symbol, name_stock as name, num as shares, price, type, total FROM stocks WHERE userid = ?", user_id)

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Getting the required quote
        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("please provide symbol for quote", 400)
        else:
            return render_template("quoted.html", name=quote["name"], symbol=quote["symbol"], price=quote["price"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        name = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        # Query the database for the entered username to validate an already existing user
        rows = db.execute("SELECT * FROM users where username = ?", name)

        # Ensure username was submitted
        if not name:
            return apology("please provide username", 400)

        elif len(rows) != 0:
            return apology("user already exists", 400)

        # Ensure password was submitted
        elif not password:
            return apology("please provide password", 400)

        # Ensure password was submitted
        elif not confirm:
            return apology("please provide confirmation password", 400)

        # Ensure the passwords that are entered match
        elif (password != confirm):
            return apology("passwords do not match", 400)

        else:
            password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

            # Query database for username
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?);", name, password_hash)
            return redirect("/")
    else:
        # Return for all GET requests for registration page
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    if request.method == "POST":
        # Get the quote price of the share and the number of shares to buy
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Please enter valid symbol", 400)

        try:
            price = float(lookup(symbol)["price"])
        except:
            return apology("Error occured while retrieving price", 400)

        try:
            name = lookup(symbol)["name"]
        except:
            return apology("Error occured while retrieving name of share", 400)

        try:
            shares = int(shares)
        except:
            return apology("shares must be a positive integer", 400)

        cost = price * shares

        user_shares = db.execute("SELECT SUM(num) as user_shares FROM stocks WHERE symbol = ? AND userid =?",
                                 symbol.lower(), user_id)[0]["user_shares"]
        if user_shares == None:
            user_shares = 0
        else:
            user_shares = int(user_shares)
        print(user_shares)

        # Print apology if the user does not have enough shares
        if not shares:
            return apology("Not a valid number of shares", 400)
        elif shares < 0:
            return apology("Please enter positive number of shares", 400)
        elif shares > user_shares:
            return apology("You do not have enough shares", 400)

        db.execute("INSERT INTO stocks (userid, symbol, num, price, type, name_stock, total) VALUES (?,?,?,?,?,?,?)",
                   user_id, symbol.lower(), -shares, price, "sell", name, -cost)
        user_cash = float(db.execute("SELECT cash FROM users where id = ?", user_id)[0]["cash"])
        print(user_cash)
        user_cash = user_cash + cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash, user_id)
        return redirect("/")
    else:
        stocks = db.execute("SELECT DISTINCT(symbol) FROM stocks WHERE userid = ?", user_id)
        return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
