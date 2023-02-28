from app import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(20), index=True, unique=True)
    passwd = db.Column(db.String(20))

    def __repr__(self):
        return f'Пользователь {self.name}'