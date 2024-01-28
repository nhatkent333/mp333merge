# app.py
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from pydub import AudioSegment
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    if 'files[]' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('files[]')

    # Check if at least two files are selected
    if len(files) < 2:
        return redirect(request.url)

    # Save the uploaded files
    saved_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            saved_files.append(filename)

    # Merge the files
    merged_audio = AudioSegment.silent()
    for filename in saved_files:
        audio_segment = AudioSegment.from_mp3(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        merged_audio += audio_segment

    # Save the merged audio
    merged_filename = 'merged_output.mp3'
    merged_audio.export(os.path.join(app.config['UPLOAD_FOLDER'], merged_filename), format='mp3')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
