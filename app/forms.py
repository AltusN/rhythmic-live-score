from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, DataRequired
from wtforms import SubmitField

class UploadGymMusic(FlaskForm):
    file = FileField("File", validators=[FileRequired()])
    submit = SubmitField("Upload")
