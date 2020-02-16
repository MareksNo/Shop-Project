from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])  # username field
    email = StringField('Email',
                        validators=[DataRequired(), Email()])  # email field
    password = PasswordField('Password', validators=[DataRequired()])  # Password field
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])  # Confirm Password field
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
