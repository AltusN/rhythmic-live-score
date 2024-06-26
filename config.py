import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ALLOWED_EXTENSIONS = {"aac", "alac", "aiff", "flac", "mp3", "ogg", "wav" }

    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethig something secret"

    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(basedir, 'app.db')}"
    
    try:
        UPLOAD_FOLDER = os.path.join(basedir, os.environ.get("UPLOAD_FOLDER")) 
    except (TypeError, ValueError):
        UPLOAD_FOLDER = os.path.join(basedir, 'app/uploads')

    MAX_CONTENT_LENGTH = int(os.environ.get("MAX_CONTENT_LENGTH") or 3 * 1000 * 1000)
