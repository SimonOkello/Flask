from flask import render_template
from app import app


@app.route("/")
@app.route("/home")
def index():
    user = {"username": "Miguel"}
    return render_template("index.html", title = "HomePage", user=user)