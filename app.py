from flask import Flask, render_template

from routes.auth import auth_blueprint
from routes.public_pages import public_pages_blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(auth_blueprint)

app.register_blueprint(public_pages_blueprint)

app.secret_key = '1234567890'

if __name__ == '__main__':
    app.run(debug=True)
    
'''
(IMPORTANT) How to fix access was denied issue:

lsof -i :5000 | grep LISTEN

sudo kill -9 (first number)

python3 app.py
'''