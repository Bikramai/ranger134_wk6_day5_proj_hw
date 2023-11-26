from flask import Blueprint, render_template, request, redirect, flash 
from werkzeug.security import check_password_hash 
from flask_login import login_user, logout_user 

#here request singulr means internal request
#redirect - someone successfully signup we redirect to signin page and redirect to shop page.
#flash display different messages to help them figure out



#internal import 
from myshop_shop.models import User, db 
from myshop_shop.forms import RegisterForm, LoginForm



#instantiate our blueprint
auth = Blueprint('auth', __name__, template_folder='auth_templates') #template folder is navigating to where html files are located


@auth.route('/signup', methods=['GET', 'POST']) # '/signup' means endpoint and the routes takes 2 methods that is GET request and POST request
def signup():                                   # GET request is bydefault actulally when you go to url that is thGET request
                                                # it also handle POST request coz we are creating data in our database

    #we need to instantiate our form as an object in order to use it
    registerform = RegisterForm() #equal to the class of register form

    if request.method == 'POST' and registerform.validate_on_submit():
        #if the request.method changes to a POST and registerform(means calling on boject).
        #if the all are validates are true then our form validated. then goes to POST method
        
        #grabbing our data from our form after it was submitted 
        first_name = registerform.first_name.data 
        last_name = registerform.last_name.data 
        username = registerform.username.data #this is the variables housing user whatever data put in a form until we pass into the class
        email = registerform.email.data       #this is the variables housing user put in a form until we pass into the class
        password = registerform.password.data 

        print(email, password, username)

        #query into database to check for username &/or email that already exists

        if User.query.filter(User.username == username).first(): #traversing means iterating over the data
            flash(f"Username already exists. Please Try Again", category='warning')
            return redirect('/signup') #basically reload the page so they can refill out the form or empty out the form
        if User.query.filter(User.email == email).first():
            flash("Email already exists. Please Try Again", category='warning')
            return redirect('/signup') 
        
        
        #we can now instantiate a new user object!!!   
        #check out the models.py/Class User/#INSERT INTO User() Values()
        # /def __init__(self, username, email, password, first_name="", last_name=""):that should be match exactly the same 
        #so we passing through these below parameters.
        user = User(username, email, password, first_name, last_name) #(going back OOP)

        #now we can add our user object to our database
        db.session.add(user) #think of this like "git add ."
        db.session.commit() #think of this like "git commit"


        flash(f"You have successfully registered user {username}", category='success')
        return redirect('/signin')
    
    return render_template('sign_up.html', form=registerform )
    #we are able to pass in anydata types string, dict this case we passing object
    #and passing it over to html that we refer forms - myshop_shop/blueprints/auth/auth_templates/sign_up.html/
    # {{ form.hidden_tag()}}>{{ form.first_name.label()}}>{{ form.first_name(class='form-control mt-2, placeholder='John')}}


@auth.route('/signin', methods=['GET', 'POST'])
def signin():

    #instantiate my loginform
    loginform = LoginForm() #login form from sign_in.html


    if request.method == 'POST' and loginform.validate_on_submit():
        #grab our data from the form
        email = loginform.email.data
        password = loginform.password.data 
        print("login info", email, password)

        user = User.query.filter(User.email == email).first() #just you gave us


        if user and check_password_hash(user.password, password): 
            #this is where we are using our UserMixin class & load_user() function
            login_user(user) #this is now saved as current_user everywhere in our application 
            flash(f"Successfully logged in {email}", category='success') 
            return redirect('/') #so if a user successfully logs in, we are going to send them home 
        else:
            flash("Invalid Email or Password, Please Try Again", category='warning')
            return redirect('/signin')
    
    return render_template('sign_in.html', form=loginform )


@auth.route('/logout')
def logout(): #giving the function name
    logout_user()
    return redirect('/')

# Next step We need to register our off blueprint/routes in __init__.py -
# from .blueprints.auth.routes import auth 
# app.register_blueprint(auth)
 