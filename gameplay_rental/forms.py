from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class GameForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
    search_precise = BooleanField('Search precise', validators=[DataRequired()])
    search_exact = BooleanField('search exact', validators=[DataRequired()])
    platforms = StringField('platforms', validators=[DataRequired()])
    stores = StringField('stores', validators=[DataRequired()])
    developers = StringField('developers', validators=[DataRequired()])
    dates = StringField('dates', validators=[DataRequired()])
    publishers = StringField('publishers', validators=[DataRequired()])