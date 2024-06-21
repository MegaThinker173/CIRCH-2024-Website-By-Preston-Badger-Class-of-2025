from flask import render_template


def render_organizers_page(route_name):
    return render_template('organizers.html', route_name=route_name)