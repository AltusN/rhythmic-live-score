import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ALLOWED_EXTENSIONS = {"mp4", "txt"}

    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethig something secret"

    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(basedir, 'app.db')}"
    
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or os.path.join(basedir, 'temp_upload')

    MAX_CONTENT_LENGTH = os.environ.get("MAX_CONTENT_LENGTH") or 3 * 1000 * 1000
    MAX_CONTENT_LENGTH = int(MAX_CONTENT_LENGTH)
