from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS 
from flask_jwt_extended import JWTManager 



#internal imports
from .blueprints.site.routes import site # to grab out site blueprint
from .blueprints.auth.routes import auth
from .blueprints.api.routes import api
from config import Config
from .models import login_manager, db
from .helpers import JSONEncoder



#instantiating our Flask app
app = Flask(__name__) 
# passing in the __name__ variable which just takes the name of the folder we're in
app.config.from_object(Config) #interpret the class as our configuration object 
jwt = JWTManager(app) #allows our app to use JWTManager from anywhere (added security for our api routes)


#wrap our app in login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in' #this referencing the blurprint auth and then the routes signin.basically saying the visitor sign in.
login_manager.login_message = "Hey you! Log in please!"
login_manager.login_message_category = 'warning' #keeping track of if there is current user it will not show up.


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# We can also comment out the above because this is rendering to the same
# location as our site blueprint. 

app.register_blueprint(site) #add this here to register your site blueprint
app.register_blueprint(auth)
app.register_blueprint(api)



#instantiating our database & wrapping our app
db.init_app(app) #initializing out app
migrate = Migrate(app, db) # basically what we are connecting!! here we need 2 args app and db.
app.json_encoder = JSONEncoder  #we are not instantiating an object we are simply pointing to this class we made when we need to encode data objects
cors = CORS(app) #Cross Origin Resource Sharing aka allowing other apps to talk to our flask app/server


#this is basically secret souce being able to migrate our sqlachemy code, flask code, python code
#that we did in models imgrating all that good stuffs to our database.
#let's hop on our Elephant sql after




# Next step go to navbar.html - templates/navbar.html