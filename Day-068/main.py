from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONFIGURING LOGIN
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    # If path is POST
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the email is already registered
        user = User.query.filter_by(email=email).first()

        # If email exists, send user to login
        if user:
            flash("Email already exists. Log in instead!")
            return redirect(url_for('login'))

        # If email doesn't exist, create the account and add it to DB
        else:
            new_user = User(name=name,
                            email=email,
                            password=generate_password_hash(password=password,
                                                            method='pbkdf2:sha256',
                                                            salt_length=8))
            db.session.add(new_user)
            db.session.commit()

            # Log in the new user
            login_user(new_user)
            return redirect(url_for('secrets'))

    # If path is GET
    else:
        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    # If POST
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if there is a user with that email in DB
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the password is matching
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)
                return redirect(url_for('secrets'))

            # If the user's password is wrong
            else:
                flash("Invalid password. Please try again.")
                return redirect(url_for('login'))

        # If the user doesn't exist
        else:
            flash("Invalid email. Please try again.")
            return redirect(url_for('login'))
    else:
        return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user_name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', filename='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
