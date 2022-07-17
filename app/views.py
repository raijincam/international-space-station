from flask import Blueprint
from flask import render_template, request, flash

from .forms import LoginForm, RegisterForm
from .models import User

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='Home')

@page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        print(f"Nueva sesión creada. Usuario: {form.username.data}")

    return render_template('auth/login.html', title='Login', form=form)

@page.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User.create_user(
            form.username.data,
            form.password.data,
            form.email.data
        )

        flash(f'The user have been created successfully.')

    return render_template('auth/signup.html', title='Sign Up', form=form)