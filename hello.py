from flask import Flask
from flask import send_file, send_from_directory, current_app
import os

app = Flask(__name__)

# http://localhost:5000/downlaod/a.rar
@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    uploads = os.path.join(current_app.root_path, './source')
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/')
def hello_world():
    return 'Hello, World!'