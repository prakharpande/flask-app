from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class register_form(FlaskForm):

    def validate_username(self, username_to_check):
        user  = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username Already Exists! Please try a different Username")
    
    def validate_email(self, email_to_check):
        user  = User.query.filter_by(email_address=email_to_check.data).first()
        if user:
            raise ValidationError("Email Already Exists! Please try a different Email")

    username = StringField(label='User Name:',validators=[Length(min=2,max=30),DataRequired()])
    email = StringField(label='Email Address:',validators=[Email(),DataRequired()])
    password1 = PasswordField(label = 'password:',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label = 'confirm password:',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label ='Create Account')

class login_form(FlaskForm):

    username = StringField(label='User Name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')