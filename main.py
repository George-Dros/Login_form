from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_bootstrap import Bootstrap5

def validate_email(form, field):
    if "@" and "." not in field.data:
        raise ValidationError(f"Email must contain the '@, .' characters")

def validate_password(form, field):
    if len(field.data) < 8:
        raise ValidationError(f"Password must be more than 8 characters long")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validate_email])
    password = PasswordField('Password', validators=[DataRequired(), validate_password])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "any-string-secret"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    submit = login_form.validate_on_submit()
    if submit:
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return  render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
