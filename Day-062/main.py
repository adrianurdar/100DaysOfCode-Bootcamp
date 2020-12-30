from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name',
                       validators=[DataRequired()])
    cafe_location = StringField('Cafe location on Google Maps (URL)',
                                validators=[DataRequired(),
                                            URL(message='Please check your URL')])
    opening_time = StringField('Opening Time e.g. 8AM',
                               validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5PM',
                               validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                choices=['☕️',
                                         '☕️☕️',
                                         '☕️☕️☕️',
                                         '☕️☕️☕️☕️',
                                         '☕️☕️☕️☕️☕️'],
                                validators=[DataRequired()])
    wifi_strength = SelectField('Wifi Strength Rating',
                                choices=['✘',
                                         '💪',
                                         '💪💪',
                                         '💪💪💪',
                                         '💪💪💪💪',
                                         '💪💪💪💪💪'],
                                validators=[DataRequired()])
    power = SelectField('Power Socket Availability',
                        choices=['✘',
                                 '🔌',
                                 '🔌🔌',
                                 '🔌🔌🔌',
                                 '🔌🔌🔌🔌',
                                 '🔌🔌🔌🔌🔌'],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_location = form.cafe_location.data
        opening_time = form.opening_time.data
        closing_time = form.closing_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_strength.data
        power_rating = form.power.data
        fields = [cafe_name, cafe_location, opening_time, closing_time, coffee_rating, wifi_rating, power_rating]
        with open('cafe-data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
        return redirect('cafes')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, length=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True)
