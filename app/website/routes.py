from flask import Blueprint, current_app, render_template

website = Blueprint('website', __name__)

@website.route('/')
def index():
    return render_template('home.html')