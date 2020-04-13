import os
from flask import render_template, request, redirect, url_for, flash
from app import app, db
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from .forms import ProfileForm
from werkzeug.utils import secure_filename
from app.models import UserProfile


@app.route('/')
def home():
    return render_template('home.html')
    
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profiles/')
def profiles():
    users =list( db.session.query(UserProfile).all())
    return render_template('profiles.html',users=users)
    
    
@app.route('/profile/',methods=['GET','POST'])
def profile():
    form=ProfileForm()
    
    if request.method == 'POST':
        print(form)
        
        #if form.validate_on_submit():
        if True:
            
            firstname = form.firstname.data
            lastname= form.lastname.data
            gender= form.gender.data
            email = form.email.data
            location = form.location.data
            bio= form.bio.data
            image = form.image.data
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            user = UserProfile(firstname, lastname, gender, email, location, bio, filename)
            db.session.add(user)
            db.session.commit()
            
            flash('Your profile was sucessfully created!')  
            return redirect('/profiles')
        flash_errors(form)
    return render_template('profile_form.html',form=form)
    

    
@app.route('/viewprofile/')
def profiled():
    return render_template('profile.html')
    

@app.route('/profile/<userid>')
def profileid(userid):
    user=db.session.query(UserProfile).filter_by(userid=int(userid)).first()
    return render_template('profile.html',user=user)
    

def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + 'app/static/uploads'):
        for file in files:
            print (os.path.join(subdir, file))



# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
