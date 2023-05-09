from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64),unique = True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(128))
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()