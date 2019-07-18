from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, usd

# Configure application
app = Flask(__name__)


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
db = SQL("sqlite:///invoice.db")


@app.route("/")
@login_required
def index():
    """Greets the user and displays the home page (four buttons)"""

    first_name = db.execute("SELECT first_name FROM users WHERE id = :user_id", user_id=session["user_id"])

    name = first_name[0]["first_name"]

    return render_template("index.html", name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

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
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        pas = generate_password_hash(request.form.get("password"))
        company = request.form.get("company")
        address = request.form.get("address")
        city = request.form.get("city")
        country = request.form.get("country")
        first_name = request.form.get("ceofirst")
        last_name = request.form.get("ceolast")

        new_user = db.execute("INSERT INTO users (username, hash, company, address, city, country, first_name, last_name) VALUES \
                              (:username, :pas, :company, :address, :city, :country, :first_name, :last_name)",
                              username=request.form.get("username"), pas=generate_password_hash(request.form.get("password")),
                              company=company, address=address, city=city, country=country, first_name=first_name,
                              last_name=last_name)

        if not new_user:
            return apology("Username taken!")

        session["user_id"] = new_user

        return redirect("/")

    else:

        return render_template("register.html")


@app.route("/items", methods=["GET", "POST"])
@login_required
def items():
    """Lists and adds items"""

    if request.method == "POST":

        # Extracting parameters from the submitted form
        item = request.form.get("item")
        price = request.form.get("price")
        user_id = session["user_id"]

        # Inserting the parametes into database
        db.execute("INSERT INTO items (item, price, user_id) VALUES (:item, :price, :user_id)", item=item, price=price,
                   user_id=user_id)

        # Extracts items from database and passes them to template
        items = db.execute("SELECT * FROM items WHERE user_id = :user_id ORDER BY item", user_id=user_id)

        return render_template("items.html", items=items)

    else:

        user_id = session["user_id"]

        items = db.execute("SELECT * FROM items WHERE user_id = :user_id ORDER BY item", user_id=user_id)

        return render_template("items.html", items=items)


@app.route("/customers", methods=["GET", "POST"])
@login_required
def customers():
    """Lists and adds customers"""

    if request.method == "POST":

        # Getting the parameters from the submitted form
        customer = request.form.get("customer")
        address = request.form.get("address")
        city = request.form.get("city")
        country = request.form.get("country")
        user_id = session["user_id"]

        # Inserting the parameters into database
        db.execute("INSERT INTO customers (customer, address, city, country, user_id) VALUES (:customer, :address, :city, \
                    :country, :user_id)", customer=customer, address=address, city=city, country=country, user_id=user_id)

        # Extracting customers from database and passes them to template
        customers = db.execute("SELECT * FROM customers WHERE user_id = :user_id ORDER BY customer", user_id=user_id)

        return render_template("customers.html", customers=customers)

    else:

        user_id = session["user_id"]

        customers = db.execute("SELECT * FROM customers WHERE user_id = :user_id ORDER BY customer", user_id=user_id)

        return render_template("customers.html", customers=customers)


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Generates invoices"""

    if request.method == "POST":

        # Getting the customer from the submitted form
        customer = request.form.get("customer")

        time = datetime.now()

        # Getting the items from the submitted form
        item1 = request.form.get("item1")
        item2 = request.form.get("item2")
        item3 = request.form.get("item3")
        item4 = request.form.get("item4")
        item5 = request.form.get("item5")

        # Getting the quantities from the submitted form
        if not request.form.get("quantity1"):
            quantity1 = float(0)
        else:
            quantity1 = float(request.form.get("quantity1"))

        if not request.form.get("quantity2"):
            quantity2 = float(0)
        else:
            quantity2 = float(request.form.get("quantity2"))

        if not request.form.get("quantity3"):
            quantity3 = float(0)
        else:
            quantity3 = float(request.form.get("quantity3"))

        if not request.form.get("quantity4"):
            quantity4 = float(0)
        else:
            quantity4 = float(request.form.get("quantity4"))

        if not request.form.get("quantity5"):
            quantity5 = float(0)
        else:
            quantity5 = float(request.form.get("quantity5"))

        user_id = session["user_id"]

        # Getting the item list and the customer list which will be passed to the dropdown menu
        items = db.execute("SELECT * FROM items WHERE user_id = :user_id ORDER BY item", user_id=user_id)
        customers = db.execute("SELECT * FROM customers WHERE user_id = :user_id ORDER BY customer", user_id=user_id)

        # Extracting the item price
        price1 = db.execute("SELECT price FROM items WHERE item = :item AND user_id = :user_id", item=item1, user_id=user_id)
        price2 = db.execute("SELECT price FROM items WHERE item = :item AND user_id = :user_id", item=item2, user_id=user_id)
        price3 = db.execute("SELECT price FROM items WHERE item = :item AND user_id = :user_id", item=item3, user_id=user_id)
        price4 = db.execute("SELECT price FROM items WHERE item = :item AND user_id = :user_id", item=item4, user_id=user_id)
        price5 = db.execute("SELECT price FROM items WHERE item = :item AND user_id = :user_id", item=item5, user_id=user_id)

        if not price1:
            price1 = 0
        else:
            price1 = float(price1[0]["price"])

        if not price2:
            price2 = 0
        else:
            price2 = float(price2[0]["price"])

        if not price3:
            price3 = 0
        else:
            price3 = float(price3[0]["price"])

        if not price4:
            price4 = 0
        else:
            price4 = float(price4[0]["price"])

        if not price5:
            price5 = 0
        else:
            price5 = float(price5[0]["price"])

        # Defining VAT (25%)
        vat = 0.25
        vatpercent = "25%"

        # Calculating the VAT per unit
        unitvat1 = price1 * vat
        unitvat2 = price2 * vat
        unitvat3 = price3 * vat
        unitvat4 = price4 * vat
        unitvat5 = price5 * vat

        # Calculating the total VAT per item
        totalvat1 = unitvat1 * quantity1
        totalvat2 = unitvat2 * quantity2
        totalvat3 = unitvat3 * quantity3
        totalvat4 = unitvat4 * quantity4
        totalvat5 = unitvat5 * quantity5

        # Computing the total VAT for the invoice
        totalvat = totalvat1 + totalvat2 + totalvat3 + totalvat4 + totalvat5

        # Computing the sale price (price + VAT)
        price1total = price1 * (1 + vat)
        price2total = price2 * (1 + vat)
        price3total = price3 * (1 + vat)
        price4total = price4 * (1 + vat)
        price5total = price5 * (1 + vat)

        # Computing the total price per item
        subtotal1 = price1 * quantity1
        subtotal2 = price2 * quantity2
        subtotal3 = price3 * quantity3
        subtotal4 = price4 * quantity4
        subtotal5 = price5 * quantity5

        # Computing the total value of the invoice (no VAT)
        subtotal = subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5

        # Computing the total amount due (total value + total VAT)
        amount = subtotal + totalvat

        # Inserting the invoice into database
        db.execute("INSERT INTO invoices (user_id, customer, vat_percent, item1, quantity1, price1, price1total, total1, \
                    item2, quantity2, price2, price2total, total2, \
                    item3, quantity3, price3, price3total, total3, \
                    item4, quantity4, price4, price4total, total4, \
                    item5, quantity5, price5, price5total, total5, \
                    subtotal, totalvat, amount, date, \
                    unitvat1, unitvat2, unitvat3, unitvat4, unitvat5, \
                    totalvat1, totalvat2, totalvat3, totalvat4, totalvat5) VALUES \
                    (:user_id, :customer, :vat_percent, :item1, :quantity1, :price1, :price1total, :total1, \
                    :item2, :quantity2, :price2, :price2total, :total2, \
                    :item3, :quantity3, :price3, :price3total, :total3, \
                    :item4, :quantity4, :price4, :price4total, :total4, \
                    :item5, :quantity5, :price5, :price5total, :total5, \
                    :subtotal, :totalvat, :amount, :date, \
                    :unitvat1, :unitvat2, :unitvat3, :unitvat4, :unitvat5, \
                    :totalvat1, :totalvat2, :totalvat3, :totalvat4, :totalvat5)",
                   user_id=user_id, customer=customer, vat_percent=vatpercent,
                   item1=item1, quantity1=quantity1, price1=price1, price1total=price1total, total1=subtotal1,
                   item2=item2, quantity2=quantity2, price2=price2, price2total=price2total, total2=subtotal2,
                   item3=item3, quantity3=quantity3, price3=price3, price3total=price3total, total3=subtotal3,
                   item4=item4, quantity4=quantity4, price4=price4, price4total=price4total, total4=subtotal4,
                   item5=item5, quantity5=quantity5, price5=price5, price5total=price5total, total5=subtotal5,
                   subtotal=subtotal, totalvat=totalvat, amount=amount, date=time,
                   unitvat1=unitvat1, unitvat2=unitvat2, unitvat3=unitvat3, unitvat4=unitvat4, unitvat5=unitvat5,
                   totalvat1=totalvat1, totalvat2=totalvat2, totalvat3=totalvat3, totalvat4=totalvat4, totalvat5=totalvat5)

        # Extracting parameters from database in order to pass them to template
        users = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=session["user_id"])

        clients = db.execute("SELECT * FROM customers WHERE user_id = :user_id AND customer = :customer",
                             user_id=user_id, customer=customer)

        invoice = db.execute("SELECT MAX(invoice_id) FROM invoices WHERE user_id = :user_id", user_id=user_id)

        invoice_no = int(invoice[0]["MAX(invoice_id)"])

        invoices = db.execute("SELECT * FROM invoices WHERE user_id = :user_id AND invoice_id = :invoice_id",
                              user_id=user_id, invoice_id=invoice_no)

        datet = db.execute("SELECT date FROM invoices WHERE user_id = :user_id AND invoice_id = :invoice_id",
                           user_id=user_id, invoice_id=invoice_no)

        date = datet[0]["date"]

        return render_template("create.html", items=items, customers=customers, users=users, customer=customer,
                               invoice_number=invoice_no, clients=clients, invoices=invoices, date=date)

    else:

        user_id = session["user_id"]

        customers = db.execute("SELECT * FROM customers WHERE user_id = :user_id ORDER BY customer", user_id=user_id)

        items = db.execute("SELECT * FROM items WHERE user_id = :user_id ORDER BY item", user_id=user_id)

        return render_template("create.html", items=items, customers=customers)


@app.route("/invoices", methods=["GET", "POST"])
@login_required
def invoices():
    """Displays selected invoice"""

    if request.method == "POST":

        user_id = session["user_id"]

        # Extracting invoices in order to pass them to templates
        invoice_list = db.execute("SELECT * FROM invoices WHERE user_id = :user_id", user_id=user_id)

        # Getting invoice number from the submitted form
        if not request.form.get("invoice"):
            invoice_no = -1
        else:
            invoice_no = int(request.form.get("invoice"))

        # Extracting parameters from database to pass to template
        users = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)

        invoice_customer = db.execute("SELECT customer FROM invoices WHERE user_id = :user_id AND invoice_id = :invoice_id",
                                      user_id=user_id, invoice_id=invoice_no)

        customer = invoice_customer[0]["customer"]

        clients = db.execute("SELECT * FROM customers WHERE customer = :customer AND user_id = :user_id",
                             customer=customer, user_id=user_id)

        invoices = db.execute("SELECT * FROM invoices WHERE invoice_id = :invoice_id AND user_id = :user_id",
                              invoice_id=invoice_no, user_id=user_id)

        date = invoices[0]["date"]

        invoice_number = invoices[0]["invoice_id"]

        return render_template("invoices.html", invoice_list=invoice_list, users=users, clients=clients, invoices=invoices,
                               date=date, invoice_number=invoice_number)

    else:

        user_id = session["user_id"]

        invoice_list = db.execute("SELECT * FROM invoices WHERE user_id = :user_id", user_id=user_id)

        return render_template("invoices.html", invoice_list=invoice_list)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
