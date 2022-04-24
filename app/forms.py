# Add any form classes for Flask-WTF here
import email
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, FloatField, IntegerField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email, Length
from flask_wtf.file import FileAllowed, FileRequired


class CarForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField('Fullname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email('Please enter a valid email address')])
    location = StringField('Location', validators=[DataRequired(), InputRequired(), Length(max=700)])
    description =  TextAreaField('description', validators=[DataRequired(), InputRequired(), Length(max=800)])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class AddCar(FlaskForm):
    description = TextAreaField('description', validators=[DataRequired(), InputRequired()])
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    transmission = StringField('Transmission', validators=[InputRequired()])
    car_type = StringField('Car_Type', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    user_id = IntegerField('user ID', validators=[InputRequired()])

class SearchForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])   