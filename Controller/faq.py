from flask import render_template

def render_faq_page(route_name):
    return render_template('faq.html', route_name=route_name)