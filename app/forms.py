from wtforms import Form
from wtforms import validators
from wtforms.fields import EmailField

from wtforms import StringField, PasswordField, BooleanField

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50, message='El username debe tener entre 4 y 50 caracteres.')
    ])
    password = PasswordField('Password', [
        validators.DataRequired()
        ])

class RegisterForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=50)
    ])
    email = EmailField('Email', [
        validators.length(min=6, max=100),
        validators.DataRequired(message='El email es requerido'),
        validators.Email(message='Ingrese un email válido') 
    ])
    password = PasswordField('Password', [
        validators.DataRequired(message='Ingrese una contraseña'),
        validators.EqualTo('confirm_password', 'La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('', [
        validators.DataRequired('Acepte los términos y condiciones')
    ])