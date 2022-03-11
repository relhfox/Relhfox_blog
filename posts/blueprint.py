from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import Post
from models import Tag

from posts.forms import PostForm
from app import db


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_body = request.form['body']
        try:
            post = Post(title=post_title, body=post_body)
            if post.title == '':
                return redirect(url_for('posts.create_post'))
            else:
                db.session.add(post)
                db.session.commit()
        except:
            print('Произошла какая-то ошибка')
        return redirect(url_for('posts.index'))
    else:
        post_form = PostForm()
        return render_template('posts/create_post.html', form=post_form)


@posts.route('/')
def index():
    search_req = request.args.get('search')
    if search_req:
        all_posts = Post.query.filter(Post.title.contains(search_req) | Post.body.contains(search_req)).all()
    else:
        all_posts = Post.query.order_by(Post.created.desc())
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
