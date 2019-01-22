# -*- coding: utf-8 -*-
from flask import Flask
from flask import send_file, send_from_directory, current_app, render_template, request, jsonify
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
    sql = "UPDATE countnumber SET download = download + 1 WHERE name='count'"

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    uploads = os.path.join(current_app.root_path, './source')
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/downloadtimes', methods=['GET'])
def downloadtimes():
    name = request.values.get('name')
    cursor = db.cursor()
    sql = 'SELECT * FROM countnumber WHERE name="%s"' % name
    print(sql)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        num = data[4]
        resData = {
            'rescode': 0,
            'resmsg': 'success',
            'resdata': {
                'count': num
            }
        }
        return jsonify(resData)
    except:
        db.rollback()
        return 'server error'

@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()