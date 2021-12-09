from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators
from wtforms.validators import DataRequired, Email


class ContactForm(Form):
    name = StringField("Candidate Name ", [validators.DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")])

    Age = IntegerField("Age")
    language = SelectField('Programming Languages', choices=[('java', 'Java'), ('py', 'Python')])

    submit = SubmitField("Submit")
