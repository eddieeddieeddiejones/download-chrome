from flask import Flask
from flask import send_file, send_from_directory, current_app, render_template, request
import os

app = Flask(__name__)

app.debug = True

# http://localhost:5000/download/a.rar
@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    uploads = os.path.join(current_app.root_path, './source')
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/')
def hello_world():
    # return '<html><body><h1>HelloWorld</h1></body></html>'
    return render_template('hello.html')

@app.route('/test', methods=['POST'])
def down():
    name = request.form['name']
    print(name)
    return 'test succeed'

if __name__ == '__main__':
    app.run()