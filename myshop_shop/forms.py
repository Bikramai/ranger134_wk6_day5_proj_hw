# This forms.py is going to house our classes that are forms of bult.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
#This is kind of do regex for us. It is basically varify the actual email and password format(Email)
#we have password field and comfirm field though doesnt match its gonna given error to users (EqualTo)
#that why we use wtforms it comes with so much equiped with error handling and validation at the back that we can do with regular html.

#Now let' built OOP class
#creating our login & register forms 
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired(), Email()])
    password = PasswordField('Password', validators=[ DataRequired() ])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[ DataRequired() ])
    email = StringField('Email', validators= [ DataRequired(), Email()])
    password = PasswordField('Password', validators = [ DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[ DataRequired() ] )
    image = StringField('Img url **Optional')
    description = StringField('Description **Optional')
    price = DecimalField('Price', validators=[ DataRequired() ])
    quantity = IntegerField('Quantity', validators=[ DataRequired() ])
    submit = SubmitField('Submit')





# what part of backend structure do routes fall under?
# The structure is MVC Model View Controler
# answer is Controller like maps or airplane routes directing traffic  