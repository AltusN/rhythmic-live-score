import os

from flask import render_template, redirect, url_for, flash, abort, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from filetype import guess_mime

from app import app
from app.forms import UploadGymMusic

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Peanuts")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        filename = secure_filename(uploaded_file.filename)

        if is_audio_file(uploaded_file.stream) and is_allowed_file(filename):
            uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            flash("file uploaded")
            return redirect(url_for('index'))
        else:
            abort(400)
    
    return render_template("upload.html")

def is_audio_file(f_stream:FileStorage) -> bool:
    # if this cannont be loaded, then it's not a audio file
    allowed  = False
    kind = guess_mime(f_stream)
    if kind is not None:
        allowed = "audio" in kind
    
    return allowed
    
def is_allowed_file(filename:str) -> bool:
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]