import os
from flask import Flask, render_template,request
import tkinter as tk
from tkinter import messagebox

app = Flask(__name__)

# Define the allowed special characters
ALLOWED_SPECIAL_CHARACTERS = [ '@','!','$','%','^','&','*','(',')','~','`',';',':']

@app.route('/')
def index():
    return render_template('VF.html')

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

@app.route('/textcheck', methods=['GET', 'POST'])
def validate_text():
    text = request.form.get("textbo1")  # Get the entered text
    
    min_words = int(request.form.get("min"))
    max_words = int(request.form.get("max"))
    max_part_words = int(request.form.get("max_part_word"))
    max_word_length = int(request.form.get("max_word_length"))
    
    sentences = text.split(".")
    errors = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            words = sentence.split()
            sentence_errors = []
            
            # Check sentence length
            num_words = len(words)
            if num_words < min_words or num_words > max_words:
                sentence_errors.append(f"Number of words: {num_words} (min: {min_words}, max: {max_words})")
            
            # Check first word capitalization
            first_word = words[0]
            if not first_word[0].isupper():
                sentence_errors.append(f"First word not capitalized: {first_word}")
            
            # Check last character
            last_char = sentence[-1]
            if last_char not in ["?", "!", "."]:
                sentence_errors.append(f"Invalid ending character: {last_char}")
            
            # Check word length
            for word in words:
                if len(word) > max_word_length:
                    sentence_errors.append(f"Word too long: {word}")
            
            # Check comma separation and part length
            if "," in sentence:
                parts = sentence.split(",")
                for part in parts:
                    part_words = part.split()
                    if len(part_words) > max_part_words:
                        sentence_errors.append(f"Part too long: {part}")
            
            if sentence_errors:
                errors.append((sentence, sentence_errors))
    
    if errors:
        error_message = "Invalid text:\n"
        for sentence, sentence_errors in errors:
            error_message += f"\nWrong Sentence: {sentence}\n"
            for error in sentence_errors:
                error_message += f"- {error}\n"
        
        message = "Validation Error" + "\n" + error_message
        print(message)
        return render_template("text_validity.html" , msg = message)
    else:
        print(message)
        msg = "Validation Success!! Text is valid!"
        return render_template("text_validity.html" , msg = msg)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8767)
