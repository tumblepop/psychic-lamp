#!/usr/bin/env python3
import os, json
from flask import Flask, abort, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    l = os.listdir('/home/shiyanlou/files')
    with open('/home/shiyanlou/files/' + l[0]) as file1:
        new1 = json.loads(file1.read())
    with open('/home/shiyanlou/files/' + l[1]) as file2:
        new2 = json.loads(file2.read())
    titles = [new1['title'], new2['title']]
    return render_template('index.html', title_list = titles)

@app.route('/files/<filename>')
def file(filename):
    if filename == 'helloshiyanlou' or filename == 'helloworld':
        with open('/home/shiyanlou/files/' +filename + '.json') as file3:
            new3 = json.loads(file3.read())
        return render_template('file.html', content = new3)
    else:
        abort(404)
        return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


