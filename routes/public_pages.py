from flask import Blueprint, render_template

from Controller.call_for_papers import render_call_for_papers_page
from Controller.faq import render_faq_page
from Controller.home import render_home_page
from Controller.last_editions import render_last_editions_page
from Controller.organizers import render_organizers_page
from Controller.presenter_registration import (presenter_register_action,
                                               render_presenter_register_page)
from Controller.rubric import render_rubric_page
from Controller.schedule import render_schedule_page

public_pages_blueprint = Blueprint('public_pages', __name__)

@public_pages_blueprint.route('/call-for-papers')
def call_for_papers_page():
    return render_call_for_papers_page('call-for-papers')

@public_pages_blueprint.route('/home')
def home_page():
    return render_home_page('home')

@public_pages_blueprint.route('/presenter-registration')
def presenter_registration_page():
    return render_presenter_register_page('presenter-registration')

@public_pages_blueprint.route('/presenter_register/presenter-register-action', methods = ['POST'])
def presenter_registration_action():
    return presenter_register_action()

@public_pages_blueprint.route('/successful-registration')
def successful_registration_page():
    return render_template('presenter_register/successful_registration.html')

@public_pages_blueprint.route('/rubric')
def rubric_page():
    return render_rubric_page('rubric')

@public_pages_blueprint.route('/faq')
def faq_page():
    return render_faq_page('faq')

@public_pages_blueprint.route('/schedule')
def schedule_page():
    return render_schedule_page('schedule')

@public_pages_blueprint.route('/organizers')
def organizers_page():
    return render_organizers_page('organizers')

@public_pages_blueprint.route('/last-editions')
def last_editions_page():
    return render_last_editions_page('last-editions')