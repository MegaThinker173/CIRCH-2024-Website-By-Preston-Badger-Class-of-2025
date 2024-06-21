import hashlib

from flask import redirect, render_template, request, session

from Model.auth_model import create_user
from utils.session_utils import get_key


def render_register_page():
    errorMessage = get_key('error_message')
    register_form = get_key('register_form')
        
    return render_template('auth/register.html', error_message=errorMessage, register_form=register_form)

def register_action():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    phoneNumber = request.form.get('phoneNumber')
    session['error_message'] = ""
    
    session['register_form'] = {
        "username": username,
        "password": password,
        "email": email,
        "phoneNumber": phoneNumber
    }
    
    isValid = True
    
    if not username:
        session['error_message'] = session['error_message'] + "Username can't be empty\n"
        isValid = False

    if not password:
        session['error_message'] = session['error_message'] + "Password can't be empty\n"
        isValid = False

    if not email:
        session['error_message'] = session['error_message'] + "Email can't be empty\n"
        isValid = False

    if not phoneNumber:
        session['error_message'] = session['error_message'] + "Phone Number can't be empty\n"
        isValid = False

    if not isValid:
        return redirect('/auth')

    user = {
        "userName": username,
        "userEmail": email,
        "userPassword": hashlib.md5(password.encode()).hexdigest(),
        "userPhoneNumber": phoneNumber
    }

    create_user(user)
    
    return render_template('auth/test.html', username = username, password = password, email = email, phoneNumber = phoneNumber)