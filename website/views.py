from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/gallery')
def gallery():
    return render_template("gallery.html")

@views.route('/aboutme')
def about_me():
    return render_template("aboutme.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")