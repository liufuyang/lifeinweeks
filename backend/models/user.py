from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    def __init__(self, uid, password):
        self.id = uid
        self.password = password
    
    def json(self):
        return {
            'uid': self.id,
            'password': self.password
        }
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_uid(cls, uid):
        return cls.query.filter_by(id=uid).first()