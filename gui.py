from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap4
import csv
import random


app = Flask(__name__)
bootstrap = Bootstrap4(app)
#NEED THSI FOR FORSM
import os #NEED THIS FOR FORMS
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name')
    location = StringField('Location on Google Maps (URL)')
    open = StringField('Opening time e.g. 8AM')
    close = StringField('Closing time e.g. 5:30pm')
    coffee = SelectField('Coffee rating', choices=[(""), ("☕️"), ("☕️☕️"), ("☕️☕️☕️"), ("☕️☕️☕️☕️"), ("☕️☕️☕️☕️☕️"), ("✘")])
    wifi = SelectField('Wifi Strength Rating', choices=[(""), ("💪"), ("💪💪"), ("💪💪💪"), ("💪💪💪💪"), ("💪💪💪💪💪"), ("✘")])
    power = SelectField('Power Socket Availability', choices=[(""), ("🔌"), ("🔌🔌"), ("🔌🔌🔌"), ("🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌"), ("✘")])

    submit = SubmitField('Submit')

@app.route("/", methods=["GET", "POST"])
def home():
    form = CafeForm()
    return render_template("index.html", form=form)


@app.route("/<int:randomnumber>")
def random_number_page(randomnumber):
        return "<h1>You found me!</h1>" \
        "<img src='https://media.giphy.com/media/AAmhvrZzLCz1m/giphy.gif?cid=790b76110nmxzs79jk4hmb91w04kbpq1wlvsasirpe3hduiu&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"




@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        form_entries = [*form.data.values()][:-2]
        with open("cafe-data.csv", "a", encoding="utf-8") as cafe_data:
            cafe_data.write("\n")
            for _ in form_entries:
                cafe_data.write(_)
                cafe_data.write(",")
        return redirect('/')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run()