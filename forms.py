from wtforms import StringField, RadioField, BooleanField, IntegerField, SelectField, FloatField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm

class Add_Pet(FlaskForm):
# wtform to add a pet on the list

    name = StringField("Pet Name", validators = [InputRequired()])
    age = IntegerField("Pet's Age", validators = [Optional()])
    photo = StringField("Photo URL", validators = [Optional()])
    notes = StringField("Notes", validators = [Optional()])
    available = BooleanField("Is the Pet Available?", 
                             default=True)
    species = RadioField("Pet's Species Type", 
                         choices = ["dog", "cat", "porcupine"], 
                         validators = [InputRequired()])


class Edit_Pet(FlaskForm):
# wtform to edit a pet on the list

    photo = StringField("Photo URL", validators = [Optional()])
    notes = StringField("Notes", validators = [Optional()])
    available = BooleanField("Is the Pet Available?", 
                             default=True)

