from flask import render_template

def render_home_page(route_name):
    return render_template('home.html', route_name=route_name)