from flask import render_template
from app import app


@app.route("/")
@app.route("/about")
def about():
    user = {"username": "Miguel"}
    return render_template("index.html", title = "Home", user=user)