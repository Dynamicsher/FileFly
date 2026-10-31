import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
Upload_folder = os.path.join(os.getcwd(), 'shared_uploads')
app.config['Upload_folder'] = Upload_folder
app.config['Max_content_length'] = 500 * 1024 *1024

#Making sure the upload folder exists
if not os.path.exists(Upload_folder):
    os.makedirs(Upload_folder)

#View files
@app.route('/')
def index():
    files = os.listdir(app.config['Upload_folder'])
    return render_template("index.html", files=files)

#Receive files
@app.route('/upload', methods=['POST'])
def upload():
    if 'file_payload[]' not in request.files:
        return redirect(request.url)

    upload_file = request.files.getlist('file_payload[]')

    for file in upload_file:
        if file.filename == '':
            continue
        
        if file:
            cleaned_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['Upload_folder'], cleaned_name))

    return redirect(url_for('index'))

#Serve files
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(
        app.config['Upload_folder'],
        filename,
        as_attachment = True
    )

#Delete files
@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    cleaned_name = secure_filename(filename)
    file_path = os.path.join(app.config['Upload_folder'], cleaned_name)

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for('index'))

#Network initialization
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)