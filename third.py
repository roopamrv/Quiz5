from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/censor', methods=['POST'])
def censor():
    text = request.form['text']
    banned_words = request.form.getlist('banned_words')
    banned_phrases = request.form.getlist('banned_phrases')
    max_banned = int(request.form['max_banned'])

    # Remove punctuation and convert to lowercase
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    text = text.lower()

    # Remove banned words
    for word in banned_words:
        text = text.replace(word.lower(), '')

    # Remove banned phrases
    for phrase in banned_phrases:
        text = text.replace(phrase.lower(), '')

    # Count occurrences of banned words and phrases
    banned_count = sum(text.count(word.lower()) for word in banned_words) + \
                  sum(text.count(phrase.lower()) for phrase in banned_phrases)

    if banned_count > max_banned:
        flash('Exceeded maximum allowed banned words/phrases. Please call the authorities.')
        return redirect(url_for('index'))
    
    return render_template('censored.html', censored_text=text)

if __name__ == '__main__':
    app.run(debug=True)
