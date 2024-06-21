import os
from flask import render_template, redirect, flash
from flask import request, session
from Model.register_model import insert_presenter
from utils.session_utils import get_key
import hashlib
from utils.allowed_papers import allowed_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/allowed_papers'

def render_presenter_register_page(route_name):
    errorMessage = get_key('error_message')
    presenterRegisterForm = get_key('presenter_register_form')
        
    return render_template('presenter_register/presenter_register.html', error_message=errorMessage, register_form=presenterRegisterForm, route_name=route_name)

def presenter_register_action():
    presenter_full_name = request.form.get('presenter_full_name')
    presenter_password = request.form.get('presenter_password')
    presenter_email = request.form.get('presenter_email')
    presenter_phoneNumber = request.form.get('presenter_phoneNumber')
    session['error_message'] = ""
    
    session['presenter_register_form'] = {
        "presenter_full_name": presenter_full_name,
        "presenter_password": presenter_password,
        "presenter_email": presenter_email,
        "presenter_phoneNumber": presenter_phoneNumber
    }
    
    isValid = True
    
    if not presenter_full_name:
        session['error_message'] = session['error_message'] + "Presenter's Full Name can't be empty\n"
        isValid = False

    if not presenter_password:
        session['error_message'] = session['error_message'] + "Presenter's Password can't be empty\n"
        isValid = False

    if not presenter_email:
        session['error_message'] = session['error_message'] + "Presenter's Email can't be empty\n"
        isValid = False

    if not presenter_phoneNumber:
        session['error_message'] = session['error_message'] + "Presenter's Phone Number can't be empty\n"
        isValid = False
    
    if 'paper_file' not in request.files or request.files['paper_file'].filename == '':
        flash('No file selected')
        isValid = False

    if isValid:
        file = request.files['paper_file']
        
        if not allowed_file(file.filename):
            flash('Invalid file type')
            isValid = False

        if isValid:
            presenter = {
            "presenterName": presenter_full_name,
            "presenterEmail": presenter_email,
            "presenterPassword": hashlib.md5(presenter_password.encode()).hexdigest(),
            "presenterPhoneNumber": presenter_phoneNumber
            }
            insert_presenter(presenter)
            
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename) # If not using secure_filename, replace filename with file.filename
            file.save(file_path)
            
            return redirect('/successful-registration')
    else:
        return redirect('/presenter-registration')