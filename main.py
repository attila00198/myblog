from flask import Flask, redirect, url_for, render_template, request

names: list[str] = [
    "Attila",
    "Gábor",
    "Beni",
    "Józsi"
]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.route("/users/")
def users():
    names.sort()
    return render_template("users.html", users=names)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u_name = request.form.get("u_name")
        u_passwd = request.form.get("u_passwd")
        
        if u_passwd == "Krassus001$":
            return redirect(url_for("user", name=u_name))
    return render_template("login.html")


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500

app.run(debug=True)
