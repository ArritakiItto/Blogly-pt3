import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/no-image-icon-15.png"

class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name  = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
    class Post(db.Model):
        """Blog post."""

        __tablename__ = "posts"

        post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
       

    class Tag(db.Model):
        """Tag for a post."""

        __tablename__ = "tags"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.Text, nullable=False, unique=True)

        posts = db.relationship("Post", secondary="posts_tags", backref="tags")

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

    # MODELS GO BELOW!

 