from flask import Blueprint
from flask import render_template

from models import Post
from models import Tag


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    all_posts = Post.query.all()
    return render_template('posts/index.html', posts=all_posts)


@posts.route('/<slug>')
def open_post(slug):
    post_to_open = Post.query.filter(Post.slug==slug).first()
    tags_to_show = post_to_open.tags
    return render_template('posts/open_post.html', post=post_to_open, tags=tags_to_show)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag_to_open = Tag.query.filter(Tag.slug==slug).first()
    posts_of_tag = tag_to_open.posts.all()
    return render_template('posts/tag_detail.html', tag=tag_to_open, posts=posts_of_tag)
