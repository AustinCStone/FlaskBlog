#################
#### imports ####
#################

from project import db
from project.models import BlogPost
from flask import flash, request, redirect, session, url_for, render_template, Blueprint
from flask.ext.login import login_required, current_user
from form import PostForm
from project.models import BlogPost


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    error = None
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id)
        db.session.add(post)
        db.session.commit()
        # render a template
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template('index.html', posts=posts, form = form, error = error)



@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template