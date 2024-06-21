from flask import render_template

def render_call_for_papers_page(route_name):
    return render_template('call_for_papers.html', route_name=route_name)