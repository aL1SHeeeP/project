from wtforms import PasswordField, EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegisterForm(FlaskForm):
    name = StringField('Как вас зовут?', validators=[DataRequired()])
    email = EmailField('Ваша почта', validators=[DataRequired(), Email()])
    password = PasswordField('Ваш пароль', validators=[DataRequired()])
    password2 = PasswordField('Ваш пароль', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

class LoginForm(FlaskForm):
    name = StringField('Как вас зовут?', validators=[DataRequired()])
    password = PasswordField('Ваш пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')