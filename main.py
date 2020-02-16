from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'da0caa0551505add1e5a786420a19f1a'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()  # getting the Register form from forms.py and setting to a variable
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data} successfully!', category='success')  # Flash on success
        return redirect(url_for('home_page'))
    if request.method == 'POST':
        flash(f'Failed to create account! Please make sure you filled out the form correctly!',
              category='warning')  # Will flash if validation has failed and the page hasn't just been loaded
        return render_template('register.html', title='Register', form=form)  # rendering the template for registration
    else:
        return render_template('register.html', title='Register', form=form)  # rendering the template for registration


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # getting the LogIN form from forms.py and setting to a variable
    if request.method == 'POST':
        in_pass = request.form.get('password')
        in_email = request.form.get('email')
        if in_pass == 'mareks12' and in_email == 'admin@gmail.com':
            flash(f'You are now logged in as an Admin successfully!', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Failed to login', category='warning')
            return render_template('login.html', title='Login', form=form)  # rendering the template for LogIn
    else:
        return render_template('login.html', title='Login', form=form)  # rendering the template for LogIn


if __name__ == '__main__':
    app.run()
