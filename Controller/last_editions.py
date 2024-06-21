from flask import render_template


def render_last_editions_page(route_name):
    return render_template('last_editions.html', route_name=route_name)