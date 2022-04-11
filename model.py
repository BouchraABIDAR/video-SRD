from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Page(db.Model):
    created_at = db.Column(db.String)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self, created_at, id, name):
        self.name = name
        self.created_at = created_at

class Video(db.Model):
    created_at = db.Column(db.String)
    id = db.Column(db.Integer, primary_key = True)
    id_insight = db.Column(db.Integer)
    title = db.Column(db.String(100))
    page_id = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    views = db.Column(db.Integer)

    def __init__(self, created_at, id, id_insight, title, page_id, likes, views):
        self.title = title
        self.page_id = page_id
        self.created_at = created_at
        self.id_insight = id_insight
        self.likes = likes
        self.views = views
        
    