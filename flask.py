from flask import Flask
from flask import jsonify
from flask import request
from textblob import TextBlob
from textblob import Word


# define Flask app
app = Flask(__name__)


@app.route('/spellCorrect')
def spellCorrect():
    #urls should take the form '/spellCorrect?text=desir-e'
    text = request.args.get('text', '')
    words = {}
    for word in text.split():
        words[word] = Word(word).spellcheck()
        #Spelling correction is based on Peter Norvig’s “How to Write a Spelling Corrector”[1] as implemented in the pattern library.
    return jsonify(**words)


if __name__ == '__main__':

    app.run()
