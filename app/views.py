"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from fileinput import filename
from app import app, db
from flask import render_template, request, jsonify, send_file, session, flash
from app.models import Cars, Favourites, Users
from app.forms import CarForm, LoginForm, AddCar
import os
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
import time
from datetime import datetime
from wsgiref.handlers import format_date_time


###
# Routing for your application.
###
@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register', methods=['POST'])
def register():
    form = CarForm()

    if request.method == "POST":
        if form.validate_on_submit():
            username=form.username.data
            password = form.password.data
            name = form.name.data 
            email = form.email.data 
            location = form.location.data
            description=form.description.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            user = Users(username, password, name, email, location, description, filename)
            db.session.add(user)
            db.session.commit()
        flash('New User Added Successfull!', 'success')
        return jsonify({'user':user})
    return jsonify(form_errors(form)) 

@app.route('/api/auth/login', methods=['POST'])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():

     if form.username.data:
            # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data

        user = Users.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
            remember_me = False

            if 'remember_me' in request.form:
                remember_me = True
                
            login_user(user, remember=remember_me)
            next_page = request.args.get('next')
            flash('Logged in sucessfully.' 'success')
            ret = {'auth': True, 'token': user.password, 'id': user.id}
        else:
            flash('Username or Password is incorrect.', 'danger')
            # remember to flash a message to the user
            ret = {'auth': False, 'token': '', 'id': ''}
        
    return jsonify(ret)

@app.route('/api/auth/logout', methods=['POST'])
@login_required 
def logout():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/cars', methods=['GET', 'POST'])
@login_required 
def showcars():
    
    decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
    if decoded['sub'] == current_user.username:
        if request.method == "GET":
            cars = []
            returnedcars = Cars.query.all()
            for car in returnedcars:
                cars.append({
                    "id": car.id,
                    "description": car.description,
                    "year": car.year,
                    "make": car.make,
                    "model": car.model,
                    "colour": car.colour,
                    "transmission": car.transmission,
                    "car_type": car.car_type,
                    "price": car.price,
                    "photo": os.path.join(app.config['UPLOAD_FOLDER'], car.photo)[1:],
                    "user_id": current_user.id
                })
            if len(cars) >=  3:
                cars = [cars[-3], cars[-2], cars[-1]]
            return jsonify(cars),200
        elif request.method == "POST":
            formobject =  CarForm()
            if formobject.validate_on_submit():
                fileobj = request.files['photo']
                cleanedname = secure_filename(fileobj.filename)
                fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], cleanedname))
                if fileobj and (cleanedname != "" and cleanedname != " "):
                    newcar = Cars(formobject.description.data, formobject.make.data, formobject.model.data,formobject.colour.data, formobject.year.data, formobject.transmission.data, formobject.car_type.data, formobject.price.data, cleanedname, current_user.id )
                    db.session.add(newcar)
                    db.session.commit()
                    feedback = {
                        "description": formobject.description.data,
                        "year": formobject.year.data,
                        "make": formobject.make.data,
                        "model": formobject.model.data,
                        "colour": formobject.colour.data,
                        "transmission": formobject.transmission.data,
                        "type": formobject.car_type.data,
                        "price": formobject.price.data,
                        "photo": cleanedname,
                        "user_id": current_user.id
                    }
                    return jsonify(feedback),200
            return jsonify(form_errors(formobject)),401         

@app.route('/api/cars', methods=['POST'])
@login_required 
def addcars():

    form = AddCar()

    if request.method == 'POST':
      if form.validate_on_submit():
         make = form.make.data
         model = form.model.data
         colour = form.colour.data
         transmission = form.transmission.data
         car_type = form.car_type.data
         year = form.year.data
         price = form.price.data
         filename = secure_filename(photo.filename)
         photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         id = form.user_id.data

         car = Cars(make=make, model=model, colour=colour, transmission=transmission, car_type=car_type, year=year, price=price, photo= filename, user_id=user_id)
         db.session.add(car)
         db.session.commit()
         flash('Successfully added a New Car!', 'success')    
    return jsonify(message="This is the beginning of our API")

@app.route('/api/cars/<int:id>', methods=['GET'])
@login_required 
def viewcar(id):
    return jsonify(message="This is the beginning of our API")

@app.route('/api/cars/<int:id>/favourite', methods=['POST'])
@login_required 
def addfavcar(id):
    return jsonify(message="This is the beginning of our API")

@app.route('/api/search', methods=['GET'])
@login_required 
def search():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/user/<int:id>', methods=['GET'])
@login_required 
def viewuser(id):
    user = Users.query.get_or_404(id)
    return jsonify(username = user.username, password= user.password, name = user.name, email = user.email, location = user.location, bilography = user.bilography, photo = user.photo, date_joined = user.data_joined)

@app.route('/api/user/<int:id>/favourites', methods=['GET'])
@login_required 
def viewcars(id):
    return jsonify(message="This is the beginning of our API")    
    
###
# The functions below should be applicable to all Flask apps.
###
def formate_date_joined():
    """format date"""
    datetime = time.strftime("%b, %Y")
    return datetime
# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
