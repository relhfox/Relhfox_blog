from flask import Blueprint
from flask import render_template

from models import Post


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    all_posts = Post.query.all()
    return render_template('posts/index.html', posts=all_posts)


@posts.route('/<slug>')
def open_post(slug):
    post_to_open = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/open_post.html', post=post_to_open)
