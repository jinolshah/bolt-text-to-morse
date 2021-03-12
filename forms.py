from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length

class DataInput(FlaskForm):
    character = StringField("Character", 
                validators=[DataRequired(message="Enter a character"), 
                Length(min=1, max=1, message="Only one character allowed!")])
    choice = RadioField("Mode", choices=["Buzzer", "LED"])
    submit = SubmitField("Convert")
    deviceID = StringField("Your BOLT Device ID", 
                validators=[DataRequired(message="Enter your BOLT device ID"), 
                Length(min=11, max=11, message="Invalid Device ID!")])
    boltapikey = StringField("Your BOLT API key", 
                validators=[DataRequired(message="Enter your BOLT API key"), 
                Length(min=36, max=36, message="Invalid API key!")])