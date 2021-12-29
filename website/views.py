from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
# When this function is called, it renders the html in "home.html"
def home():
    return render_template("home.html")