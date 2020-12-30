from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route("/")
def index():
    all_books = Book.query.all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("book_name")
        author = request.form.get("book_author")
        rating = request.form.get("book_rating")
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))

    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    book = Book.query.filter_by(id=id).first()
    if request.method == "POST":
        new_rating = request.form.get("new_rating")
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template("edit.html", book=book)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book = Book.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

