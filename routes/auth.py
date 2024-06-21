from flask import Blueprint, render_template

from Controller.auth import register_action, render_register_page

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/auth')
def auth_page():
    return render_register_page()
    
@auth_blueprint.route('/auth/register-action', methods = ['POST'])
def handle_register():
    return register_action()