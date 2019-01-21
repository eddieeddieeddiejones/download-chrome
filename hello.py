# -*- coding: utf-8 -*-
from flask import Flask
from flask import send_file, send_from_directory, current_app, render_template, request
import os
import pymysql

import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

db = pymysql.connect('192.168.1.6', 'root', 'cft6vgy7', 'chrome')

app = Flask(__name__)

app.debug = True

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM countnumber')
    data = cursor.fetchall()
    print('Database data: %s' % data)
    db.close()

    uploads = os.path.join(current_app.root_path, './source')
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()