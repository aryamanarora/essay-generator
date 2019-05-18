from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate():
    text = request.form['text']
    processed_text = text.lower().split('.')

    with open('input.txt', 'w') as f:
        for sent in processed_text:
            f.write(sent.strip() + '\n')

    os.system('python gen.py')

    data = []
    with open('output.txt', 'r') as f:
        data = f.readlines()
    res = ""
    for i in data:
        i = str(i[0].upper() + i[1:]).strip()
        res += i + '. '
    return render_template('result.html', result=res)