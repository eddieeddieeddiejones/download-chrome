from flask import Flask
from flask import send_file, send_from_directory, current_app, render_template, request
import os

app = Flask(__name__)

app.debug = True

# @app.route('/download/<path:filename>', methods=['GET', 'POST'])
@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    uploads = os.path.join(current_app.root_path, './source')
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()