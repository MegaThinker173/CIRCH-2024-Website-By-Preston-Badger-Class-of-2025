from flask import session

def get_key(key):
    value = ""
    if key in session:
        value = session[key]
        session.pop(key)
    return value