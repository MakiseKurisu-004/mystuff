#mcppal means My Cool Python Programns ALfred
#the website name is mcppal.herokuapp.com/

from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/dictionary/')
def dictionary():
    return render_template('dictionary.html')

@app.route('/animepics/')
def animepics():
    return render_template('animepics.html')

if __name__=='__main__':
    app.run(debug=True)