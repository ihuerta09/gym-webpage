"""

Web app vulnerabilities, password complexity, logs and cryptographic algorithms. 

SDEV 300: Building Secure Python Applications
Graded Lab 8: Security and Cipher Tools 
Irving Huerta
1 Mar 2024"""

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/page1.html')
def home():
    """home function used to retrieve page 1 html"""
    return render_template('page1.html', date=datetime.now())

@app.route('/page2.html')
def page2():
    """function used to retrieve page 2 html"""
    return render_template('page2.html', date=datetime.now())

@app.route('/page3.html')
def page3():
    """function used to retrieve page 3 html"""
    return render_template('page3.html', date=datetime.now())

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    """function used to retrieve registration page"""
    return render_template('register.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    """function used to retrieve login page"""
    return render_template('login.html')

@app.route('/pwupdate.html')
def updatepassword():
    """function used to reset password"""
    return render_template('pwupdate.html')


if __name__ == '__main__':
    app.run(debug=True)
