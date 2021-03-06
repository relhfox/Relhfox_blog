from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from models import Post
from models import Tag

from posts.forms import PostForm

from app import db

from flask_security import login_required


posts = Blueprint('posts', __name__, template_folder='templates')


def pages_gen(all_posts):
    curr_page = request.args.get('page')
    if curr_page and curr_page.isdigit():
        curr_page = int(curr_page)
    else:
        curr_page = 1
    return all_posts.paginate(page=curr_page, per_page=5)


def search_result(search_req):
    return Post.query.filter(Post.title.contains(search_req) | Post.body.contains(search_req)).order_by(Post.id.desc())


@posts.route('/create', methods=['POST', 'GET'])
@login_required
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


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post_to_edit = Post.query.filter(Post.slug == slug).first_or_404()
    if request.method == 'POST':
        post_form = PostForm(formdata=request.form, obj=post_to_edit)
        post_form.populate_obj(post_to_edit)
        db.session.commit()
        return redirect(url_for('posts.open_post', slug=post_to_edit.slug))
    post_form = PostForm(obj=post_to_edit)
    return render_template('posts/create_post.html', post=post_to_edit, form=post_form)


@posts.route('/')
def index():
    search_req = request.args.get('search')
    if search_req:
        all_posts = search_result(search_req)
    else:
        all_posts = Post.query.order_by(Post.id.desc())
    all_pages = pages_gen(all_posts)
    return render_template('posts/index.html', pages=all_pages, search=search_req)


@posts.route('/<slug>')
def open_post(slug):
    post_to_open = Post.query.filter(Post.slug == slug).first_or_404()
    tags_to_show = post_to_open.tags
    search_req = request.args.get('search')
    if search_req:
        all_posts = search_result(search_req)
        all_pages = pages_gen(all_posts)
    else:
        all_pages = None
    return render_template('posts/index.html', post=post_to_open, tags=tags_to_show, pages=all_pages, search=search_req)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag_slug = slug
    tag_to_open = Tag.query.filter(Tag.slug == slug).first_or_404()
    search_req = request.args.get('search')
    if search_req:
        all_posts = search_result(search_req)
    else:
        all_posts = Post.query.filter(Post.tags.contains(tag_to_open)).order_by(Post.id.desc())
    all_pages = pages_gen(all_posts)
    return render_template('posts/index.html', tag=tag_to_open, slug=tag_slug, pages=all_pages, search=search_req)
