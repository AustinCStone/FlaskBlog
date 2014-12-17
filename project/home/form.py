from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired


class PostForm(Form):
    title = TextField('title', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])