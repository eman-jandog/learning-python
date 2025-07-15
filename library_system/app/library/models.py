from app.app import db

class Book(db.Model):
    __tablename__ = 'books'
    bid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)

    def describe(self):
        return f'${self.title} by ${self.author}'