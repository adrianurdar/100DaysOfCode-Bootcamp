from flask import Flask, render_template
import requests
from datetime import datetime


app = Flask(__name__)

# Current year
current_year = datetime.today().year

# Get blog posts
posts_url = "https://api.npoint.io/5abcca6f4e39b4955965"
res = requests.get(url=posts_url)
res.raise_for_status()
posts = res.json()


@app.route('/')
def home():
    return render_template("index.html",
                           posts=posts,
                           year=current_year)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    return render_template("post.html",
                           posts=posts,
                           post_id=post_id,
                           year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
