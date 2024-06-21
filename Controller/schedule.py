from flask import render_template


def render_schedule_page(route_name):
    return render_template('schedule.html', route_name=route_name)