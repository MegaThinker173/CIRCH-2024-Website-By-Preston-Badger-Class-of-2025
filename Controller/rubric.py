from flask import render_template

def render_rubric_page(route_name):
    return render_template('rubric.html', route_name=route_name)