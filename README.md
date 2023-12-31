# Spice Magic

### Table of contents

- [Overview](https://github.com/fokhrun/restaurant_reservation#overview-)
- [Requirements](https://github.com/fokhrun/restaurant_reservation#overview-)
    - [Functional Requirements](https://github.com/fokhrun/restaurant_reservation#functional-requirements-)
    - [Technical Requirements](https://github.com/fokhrun/restaurant_reservation#technical-requirements-)
- [Tecnical Design](https://github.com/fokhrun/restaurant_reservation#tecnical-design-)
    - [High-Level Tech Stack](https://github.com/fokhrun/restaurant_reservation#high-level-tech-stack-)
    - [High-Level Architecture](https://github.com/fokhrun/restaurant_reservation#high-level-architecture-)
- [Key Implementation Aspects](https://github.com/fokhrun/restaurant_reservation#key-implementation-aspects-)
    - [Code Repository Structure](https://github.com/fokhrun/restaurant_reservation#code-repository-structure-)
    - [Flask App Factory](https://github.com/fokhrun/restaurant_reservation#flask-app-factory-)
        - [Flask Blueprints](https://github.com/fokhrun/restaurant_reservation#flask-blueprints-)
    - [Application Script](https://github.com/fokhrun/restaurant_reservation#application-script-)
    - [Data Model](https://github.com/fokhrun/restaurant_reservation#data-model-)
        - [Database Management](https://github.com/fokhrun/restaurant_reservation#database-management-)
    - [Flask Templates](https://github.com/fokhrun/restaurant_reservation#flask-templates-)
    - [Base Template](https://github.com/fokhrun/restaurant_reservation#base-template-)
    - [Handling Authentications](https://github.com/fokhrun/restaurant_reservation#handling-authentication-)
        - [Authentication Related Flask Libraries](https://github.com/fokhrun/restaurant_reservation#authentication-related-flask-libraries-)
        - [Password Security](https://github.com/fokhrun/restaurant_reservation#password-security-)
        - [Authentication Blueprint](https://github.com/fokhrun/restaurant_reservation#authentication-blueprint-)
        - [User Authentication](https://github.com/fokhrun/restaurant_reservation#user-authentication-)
        - [Protecting Routes](https://github.com/fokhrun/restaurant_reservation#protecting-routes-)
        - [Login and Registration Form](https://github.com/fokhrun/restaurant_reservation#login-and-registration-form-)
        - [Authentication Templates](https://github.com/fokhrun/restaurant_reservation#authentication-templates-)
    - [Handling Reservation](https://github.com/fokhrun/restaurant_reservation#handling-reservation-)
- [Developer Guide](https://github.com/fokhrun/restaurant_reservation#developer-guide-)
    - [Developer Environment](https://github.com/fokhrun/restaurant_reservation#developer-environment-)
    - [VSCode Debugger](https://github.com/fokhrun/restaurant_reservation#vscode-debugger-)
    - [Language And Library Requirements](https://github.com/fokhrun/restaurant_reservation#language-and-library-requirements-)
    - [Working With Styling](https://github.com/fokhrun/restaurant_reservation#working-with-styling-)
    - [Testing And Validation](https://github.com/fokhrun/restaurant_reservation#testing-and-validation-)
        - [Running Tests](https://github.com/fokhrun/restaurant_reservation#running-tests-)
        - [Test Cases](https://github.com/fokhrun/restaurant_reservation#test-cases-)
- [Deployment to Production](https://github.com/fokhrun/restaurant_reservation#deployment-to-production-)
    - [Preparation For Heroku Deployment](https://github.com/fokhrun/restaurant_reservation#preparation-for-heroku-deployment-)
    - [Deployment Steps](https://github.com/fokhrun/restaurant_reservation#deployment-steps-)
    - [Preparing Production Environment](https://github.com/fokhrun/restaurant_reservation#preparing-production-environment-)
- [Bugs](https://github.com/fokhrun/restaurant_reservation#bugs)
- [Future Improvements](https://github.com/fokhrun/restaurant_reservation#future-improvements-)
- [Credits](https://github.com/fokhrun/restaurant_reservation#credits-)
- [Project Management](https://github.com/fokhrun/restaurant_reservation#project-management-)

## Overview [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

[Spice Magic](https://restaurant-binita-99be9591d7d4.herokuapp.com/) is a full-stack restaurant website. The site provides 
- the site guests to see the restaurant menu
- the site owner to manage reservations for its restaurant guests through a centrally managed reservation database
- The site provides role-based management of the reservation database

![Spice Magic Multi-Screen Screenshot](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/multi-screen.png)

## Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Functional Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The site supports three types of users:
- `visitor`: can visit publicly available pages, anyone who landed on the site
- `guest`: can reserve tables in the restaurant on his own
- `admin`: 
    - can create reservation slots 
    - can cancel anyone's reservation (to handle unforeseeable situations)
    - can book reservations on behalf of any restaurant customer (offline booking)

The site has the following pages: 
1. `home`: provides information about the restaurant, such as cuisine, menu, serving hours, contact, etc., for any site visitors
2. `registration`: registration for new guest users
3. `login`: login for both `guest` and `admin` users
    a. any user can log in using his credentials
    b. `user` who cannot be authenticated are redirected to the login page with an error message 
4. `reserve`: 
    1. `guest` can 
        - see available reservations within the next two weeks from today 
        - can see his reservations 
        - make reservations for any available time for any number of guests within the next two weeks from today
            - can add a remark about reservations
        - cancel already made reservations
        - cannot reserve a table reserved by someone else
    2. `admin` can 
        - see any reservation status of any table made by anyone
        - make reservations for anyone
            - can add a remark about reservations
        - cancel anyone's reservation
    3. `admin` can
        - create new types of tables 
        - remove any existing type of tables
        - create any new reservation slot
        - remove any existing reservation slot

### Technical Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
- The site should be a full-stack website that is inspired by the MVC framework with the following tech stack
    - Frontend implemented by HTML, CSS, and Javascript
    - Backend implemented by Python web frameworks
    - Database
- It implements application features and business logic to manage, query, and manipulate data to handle reservation information stored in the chosen database platform using an ORM tool that goes with the chosen Python framework
    - The Python code should be written consistently using the PEP8 style guide
    - The Python code should handle the bulk of the business logic
    - Adopt an MVC-like design where models, views, and controllers are isolated for flexible manipulation
    - Automated tests should be written for the bulk of the Python code
- The front end meets a good accessibility guideline, follows the principles of UX design, meets its given purpose, and provides a set of user interactions
    - Implement forms with validations to create and edit models in the backend
- It implements identification and applies authorization, authentication, and permission for users to handle reservations
    - Apply role-based login and registration functionality
    - The current login state is reflected to the user
    - Users should not be permitted to access restricted content or functionality prior to role-based login
- The site should stay reliable to changes in the code leveraging manual and automated tests
    - Test procedures should assess functionality, usability, responsiveness, and data management within the entire web application
    - Automated tests should be written for both Python and Javascript
- The code should be free of any passwords or security-sensitive information to the repository and the hosting platform
- The site should be deployed to Heroku

## Tecnical Design [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### High Level Tech Stack [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

- Front End: [Bootstrap Framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/) (HTML, CSS, Javascript)
- Back End: [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/) (Python)
    - ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Database: [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)
- Cloud: [Heroku](https://dashboard.heroku.com/apps)

### High Level Architecture [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The following diagram provides the high-level architecture diagram for the site based on the tech stack mentioned in the previous slide.

In the Flask app context, each URL corresponds to a route in the backend. There are two main groups of route families: `main` and `auth`. The `main` routes correspond to pages and their URLs about reservations and any general information about the restaurant, such as, `home`, `reserve`, `admin`, etc. The `auth` routes correspond to pages and their URLs about user authentication, such as `register`, `login`, `logout`, etc. The Flask app leverages blueprints to organize the routes. 

For each `route`, there is a controlling function in the Flask app that receives a request for a URL (with its parameters). The app, configured appropriately, invokes the correct view function. For example, for the `<site-url>/reserve` URL, it leverages the `reserve()` controlling function. Each such function makes use of a set of forms, models, and template objects. A form handles the backend aspect of some form element in the web page. For example, the page in the `<site-url>/reserve` URL has a date selector, which corresponds to a form object that defines its field data type and its validations. A model handles CRUD operations on a database table as well as additional functionality on table attributes. For example, the `reserve()` function requires authenticated login, the current state of the coming reservations, and manipulating reservations. The function interacts with models connected to user profiles and reservations. Through these models, the function interacts with actual database tables in a MySQL instance. Finally, for each URL there is an HTML template, that is rendered with the values passed by the function in the browser. While working with these the app leverages a set of configuration (environment) variables that are available only in the hosted environment.

![High-level application architecture](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/flask_app_architecture.png)

## Key Implementation Aspects [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Code Repository Structure [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

```
- app/: source code for the flask app
    - __init__.py: include app factory method where blueprints, migration handler, database handler, login manager, etc., are registered
    - models.py: include data models used in the app to interact with the database
    - main/ : placeholder for main routes /, /reserve, and /admin
        - __init__.py : define the /main blueprint (for /, /reserve, /admin routes)
        - forms.py: form objects to interact with forms in the front end
        - views.py: route handlers (controller part of MVC) for /, /reserve, and /admin 
        - errors.py: error handlers, such as 404, 500, etc.
        - *.py: other helper modules to support route handlers in views.py
    - auth/: placeholder for auth routes /login
        - __init__.py: define the /auth blueprint ()
        - view.py
    - templates/
        - *.html: views to be rendered in the site
    - static/: contains static file
        - css/: CSS file to render HTML pages in a certain style
        - images/: images to be rendered on the site
        - scss/: bootstrap theme generation files
        - script/: javascript files
- migrations/: database migration scripts
- tests/: unit tests
    - main/: tests for app/main
    - auth/: tests for app/auth
    - test*.py: tests for files in app/
- doc_images/: images for documentations
- venv/: virtual environment for the local development, should not be tracked by git
- .env/: key information to work with the flask app and local MySQL database, should not be tracked by git
- .env_template/: template for .env file containing key information to work with the flask app and local MySQL database, should not be renamed to .env
- .gitignore: files and folders to be ignored, such venv, .env
- LICENSE: source code usage and copy license
- Procfile: app run command to be used in the Heroku production environment
- runtime.txt: Python runtime to be used in the Heroku production environment
- requirements.txt: Python library (and its version) to be used in development, testing, and production environment
- config.py: configuration for Flask and MySQL in development, testing, and production environment
- initialize_db.py: database initialization script to create tables and preliminary values
- package.json: library version for node packages to be installed in the local environment using npm
- wsgi.py: main entry point to run the app through the command line
- README.md: master documentation file
```

### Flask App Factory [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Typically a flask app is created in a single-file version advocated by many sources. Such an application is created in the global scope, there is no way to apply configuration changes dynamically. So it is too late to make configuration changes, which can be important for unit tests. We deal with this problem we delaying the creation of the application by moving it into a factory function that can be explicitly invoked from the script. This not only gives the script time to set the configuration but also the ability to create multiple application instances—another thing that can be very useful during testing or running migration while the app is running.

Check `app\__init__.py` for more details.

### Flask Blueprints [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Using [Blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints/) is an effective way to define routes in the global scope in the factory app creation method. Using different blueprints for different subsystems of the application is a great way to keep the code neatly organized. As mentioned earlier, there are two view subsystems, `main` and `auth`. 

The `main` blueprint covers the common site information and reservation routes: `\`, `\menu`, `\reserve`, and `\admin`, etc. These route controllers are defined in `app\main\views.py`. Typically blueprints are defined as follows. 

```
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
```

These blueprints are then registered in the app as follows.

```
def create_app(config_name):
    # ...
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
```

Then the route handler, i.e., controllers are defined as follows:

from . import main

```
@main.route('/')
def index():
    # ..
```

Check `app\__init__.py`, `app\main\__init__.py`, `app\main\views.py`, and `app\main\erorrs.py` for more details. The `auth` blueprint covers the authentication-related routes: `\login`, `\logout`, and `\register`.  Check `app\__init__.py`, `app\auth\__init__.py`, and `app\auth\views.py` for more details.

### Application Script [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We define the application running script in `wsgi.py`, which allows us to run the app directly running the command `flask run`. 

The script begins by creating an application. The configuration is taken from the environment variable `FLASK_CONFIG`. Flask-Migrate and the custom context for the Python shell are then initialized.

```
import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG'))
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

### Data model [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The data model employed in this project is illustrated in the following diagram. It includes four tables:

- `Role`: that implements the type of the user
- `User`: that implements the user profile including authentication capabilities, has a many-to-one relationship with `Role`
- `Table`: that implements the concept of table, which brings capacity information for reservations
- `Reservation`: that implements that reservation concept that has a one-to-many relationship with `Table` and a one-to-one relationship `User`

These models are implemented as model classes using `flask-sqlalchemy`. Check those classes in `app\models.py`.In addition, there are two Enum classes that implement fixed table capacities and reservation slots.

![Data Model](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/data_model.png)

#### Database Management [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We manage MySQL database using `mysqlclient` and `alembic` libraries. It is done through the migrate object, which is created as 

```
from flask_migrate import Migrate
from app import db

migrate = Migrate(app, db)
```

When this object is created, the following commands can be executed to create the migration script.

```
1. flask db init
2. flask db migrate -m "<sample message>"
```

Whenever there is a change in Model objects, line 2 should be executed again. Once the script is ready run the command `flask db upgrade` in any environment to prepare the tables in the database.

### Flask Templates [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Flask leverages `jinja2` based [templates](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) that basically injects input from the backend to be rendered to the frontend.
It uses the `render_template` function that is typically included in a function that handles a `route`. From `index.html` is a template in `app\main\templates` that will be rendered by `render_template` a function named `index()` that is decorated with `@app.route("\")` in `views.py`. When a request for such a route comes from the site, it leverages that `index()`
which at the end will call `render_template("main.index.html")`. Note that `main` is the blueprint where the route is managed. The function can provide additional parameters as 
keyword arguments, which can be input from the front end but can also be additional parameters managed by the function.

#### Base Template [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

All the templates extend the `base.html` template as follows `{% extends "base.html" %}`. 

The base templates provide common
- <head> section, which includes the same page title and CSS 
- site navigation menu
- login/logout segment
- flash message block
- page content block that is overridden by <body> segments of other pages
- script block for jquery and Bootstrap
- script block that is imported and can be extended by other pages
- The footer section provided key information about the restaurant

The following image shows how the front page is visually extended with the site navigation menu, login/logout segment, and the footer section.

![front Screen Marked](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/front_screen_marked.png)

Note that the site navigation bar varies based on the type of users as illustrated by the following images. This goes in line with the functional requirement of the site. 

![Site Menu](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/site_menu.png)

### Handling Authentication [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The site admin can reserve tables on behalf of any restaurant guests. However, the site provides fine-grained table reservation capability to authenticated users as follows:

- Site visitors can register using their names, email addresses, and passwords known to them. 
- Registered site `guests` can log in using their email address and password to start using fine-grained reservation functionality
- `admin` is pre-created by the site admin, who maintains the site. Once it is created, the `admin` can carry out advanced tasks on the reservations.

#### Authentication Related Flask Libraries [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We use the following Python packages
- `flask-login`: managing logged-in user sessions
- `werkzeug`: password hashing and verification
- `flask-wtf`: forms for login and registration

#### Password Security [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

`werkzeug`’s security module conveniently implements secure password hashing: 
- `generate_password_hash`: takes a plain-text password and returns the password hash as a string that can be stored in the user database. 
- `check_password_hash`: takes a password hash previously stored in the database and the password entered by the user, and returns `True` indicating 
that password is correct

These functions are used in the `User` model in `app/main/models.py`.

```
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
# ...
password_hash = db.Column(db.String(128))

@property
def password(self):
    raise AttributeError('password is not a readable attribute')

@password.setter
    def password(self, password):
    self.password_hash = generate_password_hash(password)

def verify_password(self, password):
    return check_password_hash(self.password_hash, password)
```

The password hashing function is implemented through a write-only property called `password`. When this property is set, the setter method will call
the `generate_password_hash()` function and write the result to the `password_hash` field. Attempting to read the password property will return an error, 
as clearly the original password cannot be recovered once hashed.

The `verify_password()` method takes a password and passes it to the `check_password_hash()` function for verification against the hashed version stored 
in the `User` model. If this method returns True, then the password is correct.

#### Authentication Blueprint [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The routes related to the user authentication subsystem will be added to a blueprint called `auth` that manages the `login`, `logout`, and `register` routes. 

#### User Authentication [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

`flask-login` implements `is_authenticated`, `is_active`, `is_anonymous`, and `get_id` as properties and methods through `UserMixin` 
class. It needs to be implemented through `User` as follows:

```
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

flask-login needs to be initialized in the app factory function as follows. The `login_view` attribute of the `LoginManager` object sets the endpoint for the login page. Flask-Login will redirect to the login page when an anonymous user tries to access a protected page. Because the login route is inside a blueprint, it needs to be prefixed with the blueprint name.

```
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    ...
    login_manager.init_app(app)
    ...
```

`flask-login` requires the application to designate a function to be invoked when the extension needs to load a user from the database given its identifier. It is done through
the `user_loader` decorator that registers the function with `flask-login`, which will call it when it needs to retrieve information about the logged-in user. The user identifier will be passed as a string, so the function converts it to an integer before it passes it to the `SQLAlchemy` query that loads the user. The return value of the function must be the user object, or `None` if the user identifier is invalid or any other error occurred. Check out the following implementation:

```
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

For more details, check `app/main/models.py` ajd `app/__init__.py`.

#### Protecting Routes [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

To protect a route so that it can only be accessed by authenticated users, `FlaskLogin` provides a `login_required` decorator. An example of its usage follows:
```
from flask_login import login_required

@app.route('/a_protected_route')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
```

#### Login And Registration Form [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The login form that will be presented to users has a text field for the email address, a password field, a “remember me” checkbox, and a submit button. In addition, a set of validators needs to be implemented to ensure that wrong inputs are not passed. All of these are very straightforward to implement using `flask-wtf` and `wtforms`. 

Check out the following example, which is a skeleton for our implementation: 

```
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
```

Other validations have been implemented that make it safer for users to work with the login form as illustrated by the following image:
- Image 1 shows an empty form 
- Image 2 shows the state when a mandatory field is left empty. This validation has been implemented using `flask-wtf` library
- Image 3 shows the state when an input has been provided in an incorrect format. This validation has been implemented using custom Javascript in `app\static\javascript\script.js`.
- Image 4 shows the state when an incorrect input is provided. The flash message is actually returned by the controlling function after validation fails in the backend.

![Login Screen With Validations](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/login_form_multiple.png)

A similar design has been applied to the registration form as illustrated below:

![Registration Screen With Validations](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/registration_form_multiple.png)


#### Authentication Templates [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We implemented two templates namely `login.html` and `logout.html` that have similar designs. These templates can be found in the `app\templates\auth` folder. The previous section shows how the screens are rendered. The main code that handles these templates is placed in the `base.html` template using the following code snippet. 

```
<ul class="nav navbar-nav navbar-right">
{% if current_user.is_authenticated %}
<li><a href="{{ url_for('auth.logout') }}">Log Out</a></li>
{% else %}
<li><a href="{{ url_for('auth.login') }}">Log In</a></li>
{% endif %}
</ul>
```

The following image how the login and logout flow shows up in the navigation menu. 

![Login and Logout Flow](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/login_logout_flow.png)

Note that `base.html` template also provides the following script.

```
{% block scripts %}
    <script src="{{ url_for('static', filename='script.js') }}"></script>
{% endblock %}
```
This script is imported in `login.html` and `register.html` as follows. 

```
{% block scripts %}
    {{ super() }}
{% endblock %}
```

The script primarily handles custom validation on the registration and login form rendered on the page. It basically checks `username`, `email address`, and `password` to conform to a certain structure. For more details, check `app\static\javascript\script.js`.

### Handling Reservation [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The following diagram shows a wireframe of a user changing reservation.  

![Reservation wireframe](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/wireframe-reservation.png)

We implemented this wireframe into a page that interacts with the reservation table through the Flask app. The following diagram shows how an authenticated guest changes reservations. The guest does that by canceling an existing reservation, picking a new date and slot, and reserving a new one. While carrying this out the app handles request from the page session, pick the current user, run a filter query against the reservation table, and updates the reservation table to reverse slots.

![Guest Reserve Unreserve](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/guest_reserve_unreserve.png)

The admin has a slightly different view where he can see everyone's reservation, including the one he made for the offline users. The following image shows that view. 

![Admin Reserve Unreserve](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/admin_reserve_unreserve.png)

Finally, the admin can create new slots for the upcoming months, one month at a time. This page can only be accessed by the admin user. The following image shows that view.

![create New Slots](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/admin_reserve_unreserve.png)

## Developer Guide [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Developer Environment [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

1. Ensure that you have a Python version of at least `Python v3.11` and `pip v23.3.1`
2. Clone the repository https://github.com/fokhrun/restaurant_reservation.git as `restaurant_reservation` in your local directory
3. Work inside `restaurant_reservation`
4. Create a virtual environment using `venv`:
    ```
    1. python3 -m venv venv
    2. .\venv\Scripts\activate
    3. pip install -r .\requirements.txt
    ```
5. Download and install MySQL v8.0.35 or upwards from `https://dev.mysql.com/downloads/installer/`
6. Setup a database `restaurant_dev`
7. Make a copy of `.env_template` as `.env` and fill in the missing values
8. Initialize the database with the right tables and their starter values by running `python .\iniatialize_db.py`. It creates 
    - 2 roles: `Admin` and `Guests`
    - 3 users: 1 `Admin` type and 2 `Guests` type
    - 6 tables of different capacities
    - 6 (table) * 2 (slot per day) * 30 (days for November 2023) to create all reservation slots for November
9. Run the app `flask run --debug`
10. You can use `VSCode` as an editor

### VSCode Debugger [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
Debugging a Flask app in `VSCode` involves setting up a launch configuration. 
Here's an example configuration for debugging a Flask app in VSCode:

- Open your Flask project in `VSCode`
- Create a `launch.json` file inside the `.vscode` directory in your project if it doesn't exist.
- VSCode will auto-generate the `launch.json` if you provide correct options, for example, python, then Python: Flask, and wsgi.py

"""
    {
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "wsgi.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
"""
- Set breakpoints in your code by clicking in the gutter area next to the line number in VSCode.
- Start the debugger by pressing F5 or clicking on the debug icon in VSCode and selecting the Flask configuration you just created.
- This setup will allow you to debug your Flask app by running it in debug mode within VSCode.

### Language And Library Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The two main languages that leverage libraries are `Python` and `Javascript`. 

For Python, we manage libraries in `requirements.txt`. The libraries are installed in the local development environment using `pip`. It is a good idea to refresh this file whenever a package is installed or upgraded. The libraries should be installed in a virtual environment. The instructions are given in the first few steps in [Developer Environment](https://github.com/fokhrun/restaurant_reservation#developer-environment-). 

The requirements file mentions the version numbers for each of the libraries. However, the current version of flask-login is not compatible with flask > 3.0. The fixes are on the way to make it work soon. More details can be found in this [issue](https://github.com/maxcountryman/flask-login/issues/805). Until then, it is recommended to use a widely accepted [temporary fix](https://github.com/maxcountryman/flask-login/issues/809).

For Javascript, the libraries are installed using `npm`, which requires `node.js`. In this project, we leverage `bootstrap` and `node-sass`, which are installed using `npm`. Install `node.js` using this [link](https://nodejs.org/en/download). We recommend installing these packages locally. It requires defining a `package.json` file where versions of the libraries are mentioned. The packages are installed using the command `npm install <package>`, which installs it local node_modules directory, which should be included in the `.gitignore` folder.

In this project, we are working with `bootstrap@4.5`. To install `bootstrap`, run the command `npm install bootstrap` and to install `node-sass`, run the command `npm install node-sass`.

### Working With Styling [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

This project leverages `bootstrap` for default themes and `node-sass` for custom themes for styling. 

To work with Bootstrap, copy-paste the stylesheet <link> into the <head> of `base.html`, which is used in all other HTML files.

```
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
```

To work with a custom theme. e.g., to influence the coloring theme in a more custom manner than what `bootstrap` provides, we use [`SCSS`](https://www.geeksforgeeks.org/what-is-the-difference-between-css-and-scss/), which is a superset of `CSS`. As `Flask` does not support `SCSS` natively, we need to use a tool like `node-sass` to compile `SCSS` files into `CSS`. 

To add global `SCSS` in a `Flask` application, we need to compile the SCSS files into CSS files. To do that, carry out the following steps:

- Create a directory name `static` in the `app` folder, if it doesn't exist already
- Inside the `static` directory, create a `scss` directory and a `css` directory
- Put the global SCSS file named `main.scss` in the `scss` directory. For example, the following main.scss file overrides the theme color of the site
    ```
    @import "theme_color";
    @import "./node_modules/bootstrap/scss/bootstrap";
    ```
    Here the `theme_color` is another CSS file where the theme colors are defined. 

- Compile the SCSS file into a CSS file using the command `node-sass app/static/scss/main.scss app/static/css/main.css`

- To use the `main.css` overriding bootstrap themes, link to it using the url_for function. This line should be placed inside the <head> tag of `base.html`.

Here's an example of how to do this in a Jinja2 template:

```
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
```

Note that every time there is a change in the SCSS files, we need to recompile them into CSS.

### Testing And Validation [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We leverage `unittest` library for Python code testing. Some examples of vanilla usage of the `TestCase` class of the module can be found in `tests\main\test_utils.py`, which tests Python functions in `app\main\utils.py`. Often times testing requires mocking certain function calls so that the test focuses only on the logic part of the code instead of implementing all dependencies. Refer to the implementation of `TestModelUtils` in `app\main\utils.py` for testing using mock. 

#### Running Tests [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We added a custom command with Flask to run the tests by implementing the following function in `wsgi.py`.

```
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
```

To work with the tests

- Add test codes in the `tests` or its subfolders (follow the app folder structure)
- Run `flask test` or `flask test tests.<specific test folder or file inside test>` 

We also measure the test coverage using the `coverage` module. See `wsgi.test` for more details. Currently, the coverage is 32% with 27 tests. For more details, check the following:

![Test Coverage](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/test_coverage.png)

#### Test Cases [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Testing some of the functions requires an application. It requires the creation of a flask test app using the `TestConfig` in `config.py`. It can be implemented using the following class:

```
class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
```

This class can be used as `TestTableReservation(FlaskAppTestCase)`, which inherits its `setUp` and `tearDown` functions unless overridden.

We defined another class named `FlaskAppTestCaseWithModels`, which creates the test app and populates the test database with some dummy tables and entries based on our models. This class is used when the models need to be accessed. Both these classes are defined in `tests\utils.py`.

### Code Validation [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

#### Manual Testing

The following manual testing has been carried out and validated

- Interactions with site navigation have been thoroughly tested
    - Only Home (`Spice Magic`) and Restaurant `menu` navigation open to every site visitor
    - In addition to the above, the `Reserve` navigation is available to every authenticated user
    - In addition to the above, the `Admin` navigation is available to restaurant `admin` user
- Registration and Login
    - Only authenticated `guest` can be created using the registration link
    - While creating the `guest` using registration or login with an existing credential, the validations must pass to proceed
        - all entries have to be provided
        - `username` with length 5, this can be changed to a different length later on
        - `email` with the right structure
        - `password` with length 3, this can be changed to a different length later on 
        - `password` has to be confirmed by entering twice (in registration)
    - Only `registered` users can log in
    - `Admin` user can only be created using the dev team, using the initialization script or manually
- Reservation
    - All authenticated `user` can reserve any available slots
    - All authenticated `user` can unreserve their current slots
    - Only reservation `Admin` can unreserve other `user` slots
- Reservation Admin
    - Only reservation `Admin` can create new reservations
    - New reservations can be created 4 weeks ahead of time from the currently available slots

#### Front End Code Validation [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
    
- `HTML`: codes have been validated using `https://validator.w3.org/`. No errors or warnings are reported after fixing some minor mistakes.
- `CSS`: codes are generated using the `node-sass`, which makes the w3c validator `https://jigsaw.w3.org/css-validator` non-applicable. 
- `Javascript`: no automated test for javascript has been added yet. 
- Overall: The `Lighthouse` test has given a high rating higher 90 in Performance, Accessibility, and Best Practices for all pages.

#### Backend Code Readability [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The code is validated using the command `pylint --max-line-length=120`. The max line length is changed from 80 to 120 to achieve optimal 
readability in modern screens.

The following warnings have been suppressed to handle special cases:
- `# pylint: disable=C0415` in `app\__init__.py`
- `# pylint: disable=C0413, R0401` in `app\main\__init__.py`
- `# pylint: disable=W0613` in `app\main\errors.py`
- `# pylint: disable=C0121` in `app\main\model_services.py`
- `# pylint: disable=C0103, E0402, R0903` in `app\main\models.py`
- `# pylint: disable=C0413, R0401` in `app\auth\__init__.py`

Apart from these, there are no other errors or warnings reported by `pylint`.

### Deployment To Production [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

#### Preparation For Heroku Deployment [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
- runtime.txt: `Python` run time version
    - `python-3.11.6`
- procfile: app exposed as `wsgi.py` with run command using `Gunicorn`
    - `web: gunicorn wsgi:app` 
- requirement.txt: Python dependencies
    - manually crafted or run `pip freeze > requirements.txt` in the local virtualenv
- "Eco Dynos Plan" in Heroku
- GitHub account connected to Heroku for free tier

#### Deployment Steps [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
- Create a new app in [Heroku](https://dashboard.heroku.com/apps)
- Fill the form with the app name, i.e., "restaurant-binita" and "Europe" as the region
- Click [addons](https://elements.heroku.com/addons)
    - Click [JawsDB MySQL](https://elements.heroku.com/addons/jawsdb), Choose Kitefin Shared (for free plan) and Install
        - You will get access to [Kitefin Server Dashboard](https://mysql.jawsdb.com/resource/dashboard) with information on 
            - `Host`
            - `Username`
            - `Password`
            - `Port`
            - `Database`
- Select `Settings`
    - Add `heroku/python` build pack
    - Add the following config vars that mimic `.env` file in the local environment
        - `JAWSDB_URL`: `Connection String` in Kitefin Server
        - `FLASK_CONFIG`: production
        - `DATABASE PROD`: `Database` in Kitefin Server
        - `DB_HOST_PROD`: `Host` in Kitefin Server
        - `DB_PASSWORD_PROD`: `Password` in Kitefin Server
        - `DB_PASSWORD_PROD`: `Password` in Kitefin Server
        - `SECRET_KEY`: <chosen secret> 
- Select `Deploy`
    - Choose "GitHub" as deployment method
    - Search the GitHub repo name `restaurant_reservation`. Once the repo is found, connect the repo.
    - Choose the default branch to deploy, i.e., the `main` branch
    - Click "Enable Automatic Deploys" which allows the app to be redeployed for every commit.
    - Click "Deploy Branch" for the first manual push.
- Select `Open app` to verify that the app has deployed.

#### Preparing Production Environment [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

1. `gunicorn` is not supported in In Windows. you can use `waitress` instead. Follow these [guide](https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows)
2. To initialize the production database, change the `FLASK_CONFIG` to `production`
3. run `python .\iniatialize_db.py` to create the initial roles, users, tables, and reservations
4. Run the app by clicking the `Open App`
5. Verify by login to the site using the newly created credentials and checking the reservations visible to different users
6. If there are errors, click `More` and use options, such as `View logs` or `Run console`

## Bugs [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Fixed Bugs:
- Reservation status change request did not update status
- Reservation status change updated for wrong users
- New reservation slots were not created
- Accidentally removed Gunicorn that blocked production deployment
- Wrong ID used for form validation

Open Issues:
- Make the role of the `User` model non-nullable
- Front-end validation methods do not disappear at the right time
- User can reserve for past days, which should not be allowed
- Use lower-resolution images to load the site faster

## Future Improvements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

- A more consistent and richer form validation
- Add more unit tests for `app\auth\forms.py`, `app\auth\views.py`, `app\main\views.py`, `app\models.py`, `app\main\errors.py`
- Add more mocking-based tests where the database and API are involved
- Add Javascript-based validation for the login/registration pages
- Add a more elegant reservation system where a user does not have to mention which table, rather the guest number
- Add a mechanism to provide remarks for reservations
- Add a mechanism for the site admin to handle reservation requests through an approval flow
- Add an Email-based two-step registration process for new users
- Add a mechanism to reset passwords of an existing user
- Add a mechanism to remove daily, weekly, and monthly reservation slots
- Add a mechanism to send emails to users about reservation
- Add a better admin panel for creating/deleting/updating reservation slots for the admin
- Add a better way to document

## Credits [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Photos by:
1. Chan Walrus: [front_image.jpg](https://www.pexels.com/photo/white-and-brown-cooked-dish-on-white-ceramic-bowls-958545/)
3. Mareefe: [about_1.jpg](https://www.pexels.com/photo/three-condiments-in-plastic-containers-674483/)
2. Gagan Kaur: [about_2.jpg](https://www.pexels.com/photo/a-woman-cooking-indian-food-3531700/)

## Project Management [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
Initially the project management has been carried out in a local excel file. Later the notes have been migrated to the GitHub project [@fokhrun's portfolio project 4](https://github.com/users/fokhrun/projects/2). Going forward, the GitHub project should be used. 
