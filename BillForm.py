from wtforms import Form
from wtforms.fields.simple import StringField, SubmitField


class BillForm(Form):

    amount = StringField("Enter Bill Amount:")
    category = StringField("Bill Type:")
    period = StringField("Enter Bill Cycle:")

    name_1 = StringField("Enter Name: ")
    stay_duration_1 = StringField("Enter Stay Duration: ")

    name_2 = StringField("Enter Name: ")
    stay_duration_2 = StringField("Enter Stay Duration: ")

    button = SubmitField("Calculate")