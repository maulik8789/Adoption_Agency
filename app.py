from flask import request, render_template, Flask, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from wtforms import StringField, RadioField, BooleanField, IntegerField, SelectField, FloatField
from models import Pet, db, connect_db

from forms import Add_Pet, Edit_Pet

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'key'
app.config['WTF_CSRF_ENABLED'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
"""shows list of pets"""
def home():
    pets = Pet.query.all()
    return render_template("home.html", pets = pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
"""for adding a pet on the list"""
    form = Add_Pet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo = form.photo.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name = name, species = species, age = age, photo_url = photo, notes = notes, available = available)
        db.session.add(pet)
        db.session.commit()

        flash(f"A {species} named {name} has been added")
        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)


@app.route("/<pet_id>")
"""shows detail of a particular pet"""

def detail(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template("detail.html", pet = pet)

@app.route("/edit/<pet_id>", methods=["GET", "POST"])
"""shows and allows editing of a pet"""

def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = Edit_Pet()
    form.photo.data = pet.photo_url
    form.notes.data = pet.notes

    if form.validate_on_submit():
        
        pet.photo_url = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()

        flash(f"A {pet.species} named {pet.name} has been Edited")
        return redirect(f"/{pet_id}")

    else:
        flash(f"{form.errors}")

        return render_template("edit.html", form=form, pet = pet)

