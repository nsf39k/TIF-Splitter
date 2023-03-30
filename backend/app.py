from flask import request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
import zipfile
from . import create_app
from .config import Config
from .image_processing import process_geotiff

app = create_app()
app.config.from_object(Config)

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
OUTPUT_FOLDER = app.config['OUTPUT_FOLDER']
ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file provided'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        process_geotiff(os.path.join(UPLOAD_FOLDER, filename), OUTPUT_FOLDER)
        return jsonify({'message': 'File uploaded and processed successfully'}), 200

    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/download', methods=['GET'])
def download_result():
    output_directory = OUTPUT_FOLDER
    zip_filename = 'output.zip'

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(output_directory):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_directory))

    return send_from_directory('.', zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run()