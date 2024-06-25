import os

from flask import render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename


from app import app
from app.forms import UploadGymMusic

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Peanuts")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = UploadGymMusic()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        app.logger.debug(filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        flash("file uploaded")
        return redirect(url_for('index'))
    
    return render_template("upload.html", form=form)

def allowed_file(filename:str) -> bool:
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]