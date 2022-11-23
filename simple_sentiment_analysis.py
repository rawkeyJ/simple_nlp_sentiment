#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template


# In[ ]:



app = Flask(__name__,template_folder="templates", static_folder='static')

@app.route('/')
def my_form():
    return render_template('indexone.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']

    if(score > 0):
        label = 'Damn! This sentence has Positive Vibes'
        emojika = [128516]
    elif(score == 0):
        label = 'Guess What, This sentence is Neutral'
        emojika = [128511]
    else:
        label = 'Oh! This sentence has Negative Vibes'
        emojika = [128543]

    return(render_template('index.html', variable=label, emojika=emojika[0]))

if __name__ == "__main__":
    app.run()

