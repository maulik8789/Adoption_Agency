from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    """Connect the database to our Flask app."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
# pets table attributes

    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    
    name = db.Column(db.String,
                     nullable = False)

    species = db.Column(db.String,
                        nullable = False)

    photo_url = db.Column(db.String)

    age = db.Column(db.Integer)

    notes = db.Column(db.String)

    available = db.Column(db.Boolean, 
                          nullable = False, 
                          default = True)
