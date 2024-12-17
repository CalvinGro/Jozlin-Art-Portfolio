# Import necessary modules from Flask
from flask import Blueprint, render_template

# Create a Blueprint instance named 'views'
# A Blueprint allows for modular organization of routes in a Flask application
views = Blueprint("views", __name__)


# Route: Home Page
# URL: '/'
# Description: This route renders the home page (home.html)
@views.route('/')
def home():
    return render_template("home.html")   # Render the home page template

# Route: Gallery Page
# URL: '/gallery'
# Description: This route renders the gallery page (gallery.html)
@views.route('/gallery')
def gallery():
    return render_template("gallery.html")  # Render the gallery page template


# Route: About Me Page
# URL: '/aboutme'
# Description: This route renders the 'About Me' page (aboutme.html)
@views.route('/aboutme')
def about_me():
    return render_template("aboutme.html")  # Render the 'About Me' page template


# Route: Contact Page
# URL: '/contact'
# Description: This route renders the contact page (contact.html)
@views.route('/contact')
def contact():
    return render_template("contact.html")  # Render the contact page template