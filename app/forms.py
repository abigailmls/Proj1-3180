from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ProfileForm(FlaskForm):
    firstname=StringField('First Name',validators=[DataRequired()])
    lastname=StringField('Last Name', validators=[DataRequired()])
    gender=SelectField('Gender', choices=[('male', 'male'), ('female', 'female')])
    email=StringField('Email',validators=[DataRequired(),Email()])
    location =StringField('Location',validators=[DataRequired()])
    bio=TextAreaField('Biography',validators=[DataRequired()])
    image= FileField('Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
