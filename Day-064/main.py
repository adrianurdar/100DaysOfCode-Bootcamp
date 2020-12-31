from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
db = SQLAlchemy(app)


MDB_API_KEY = "6c76bca02561d0855bda2525c1807990"
MDB_API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"


class EditMovieForm(FlaskForm):
    rating = DecimalField('Your Rating Out of 10 e.g. 7.5',
                          validators=[DataRequired()])
    review = StringField('Your Review',
                         validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title',
                        validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250))


db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    form = EditMovieForm()
    movie = Movie.query.filter_by(id=id).first()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        search_movies_params = {
            "api_key": MDB_API_KEY,
            "language": "en-US",
            "query": title,
        }

        search_movies_res = requests.get(url=MDB_API_ENDPOINT, params=search_movies_params)
        search_movies_res.raise_for_status()
        data = search_movies_res.json()

        movies = data["results"]
        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)


@app.route("/select")
def select():
    movie_id = request.args.get("movie_id")
    movie_details_params = {
        "api_key": MDB_API_KEY,
    }

    movie_details_res = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params=movie_details_params)
    movie_details_res.raise_for_status()
    data = movie_details_res.json()

    new_movie = Movie(
        title=data["original_title"],
        year=int(data["release_date"].split("-")[0]),
        description=data["overview"],
        img_url=f'https://image.tmdb.org/t/p/w500{data["poster_path"]}',
    )

    db.session.add(new_movie)
    db.session.commit()

    movie_title = data["original_title"]
    movie = Movie.query.filter_by(title=movie_title).first()

    return redirect(url_for('edit', id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
