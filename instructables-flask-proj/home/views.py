<p>from flask import Blueprint, render_template</p><p>home_view = Blueprint('home_view', __name__)</p>@home_view.route('/')
def display_home_page():
	return render_template('home_page.html', num=10)