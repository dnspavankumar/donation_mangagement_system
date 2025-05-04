import os

# Secret key for Flask session
SECRET_KEY = os.environ.get('SESSION_SECRET', 'dev_key')

# SQLite database URI
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///donations.db')

# File upload settings
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size

# Flask configuration
DEBUG = True
