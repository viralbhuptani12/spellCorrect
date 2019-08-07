from flask import Flask
from flask import jsonify
from flask import request
from textblob import TextBlob
from textblob import Word


# define Flask app that does all the magic
app = Flask(__name__)


@app.route('/spellCorrect')
def spellCorrect():
    #urls should take the form '/spellCorrect?text=desir-e'
    text = request.args.get('text', '')
    words = {}
    for word in text.split():
        words[word] = Word(word).spellcheck()
    return jsonify(**words)


if __name__ == '__main__':

    app.run()