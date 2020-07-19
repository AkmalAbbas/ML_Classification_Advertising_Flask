from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError

class AdvertisingForm(FlaskForm):
    time_spend = TextField("Daily time spent on site",[validators.Required("*")])
    age = TextField("Age of customer",[validators.Required("*")])
    area_income = TextField("Income from area",[validators.Required("*")])
    internet_usage = TextField("Daily internet usage",[validators.Required("*")])
    gender = TextField("Gender",[validators.Required("*")])
    submit = SubmitField("Submit")
