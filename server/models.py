from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Validator for phone_number
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if not phone_number or not phone_number.isdigit():
            raise ValueError("Phone number must be a non-empty string of digits.")
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
    @validates('title')
    def validate_title(self, key, title):
        if not title or len(title) < 5:
            raise ValueError("Title must be a non-empty string with at least 5 characters.")
        return title

    
    @validates('category')
    def validate_category(self, key, category):
        valid_categories = ["Tech", "Science", "Art", "Other"]
        if category not in valid_categories:
            raise ValueError(f"Invalid category. Choose from {valid_categories}.")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'
