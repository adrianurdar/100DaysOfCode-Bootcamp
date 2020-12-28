from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetch all the blog posts
res = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
res.raise_for_status()
posts = res.json()


@app.route("/")
def index():
    return render_template("index.html",
                           posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html",
                           posts=posts,
                           post_id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
