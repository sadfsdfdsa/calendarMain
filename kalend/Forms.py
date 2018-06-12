from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import wtforms

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DMYForm(FlaskForm):
    submit = SubmitField('submit')
    month = wtforms.SelectField('Months', choices=['January','February','March','April','May','June','July','August','September','October','November','December'], validators=[DataRequired()])
    year = wtforms.IntegerField('year', validators=[DataRequired()])