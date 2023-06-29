import os
from flask import Flask, render_template,request

app = Flask(__name__)

# Define the allowed special characters
ALLOWED_SPECIAL_CHARACTERS = [ '@','!','$','%','^','&','*','(',')','~','`',';',':']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['GET', 'POST'])
def password_checker():
    if request.method == 'POST':
        password = request.form['psw']
        valid = is_password_valid(password)
        return render_template('VF.html', valid=valid)
    return render_template('CP.html')

def is_password_valid(password):
    # Check password length
    print(len(password))
    if len(password) < 8 or len(password) > 20:
        return False

    # Check for at least one number, uppercase letter, and two special characters
    has_number = False
    has_uppercase = False
    special_char_count = 0

    for char in password:
        if char.isdigit():
            has_number = True
        elif char.isupper():
            has_uppercase = True
        elif char in ALLOWED_SPECIAL_CHARACTERS:
            special_char_count += 1

    return has_number and has_uppercase and special_char_count >= 2

if __name__ == '__main__':
    app.run()
