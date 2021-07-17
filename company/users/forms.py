# users/form.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired. Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FiledAllowed

from flask_login import current_user
from company.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm"), message="Password must match!"])
    pass_confirm = PasswordField("Cofirm Password", validators[DataRequired()])
    submit = SubmitField("Register!")

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has ben registered already!")

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has ben registered already!")

class UpdateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    picture = FileField("Update Profile Picture", validators=[FiledAllowed(["jpg", "png"])])
    submit = SubmitField("Update Profile")
