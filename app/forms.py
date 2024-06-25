from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

class UploadGymMusic(FlaskForm):
    file = FileField("File", validators=[FileRequired()])
    submit = SubmitField("Upload")
