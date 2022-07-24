# Relhfox_blog

Demo video: https://youtu.be/IMkMUj965fw

Relhfox_blog - is a simple blog script. You are free to use it as your personal blog (no commercial use allowed). You can change it, develop anyhow you like.

It works as Flask app and uses Python interpreter on a server side, along with MySQL database. All the HTML/CSS part is made of Bootstrap components.

It uses ready-to-use extensions for admin section and login feature.

The interface language is Russian, but it won't take long to translate it to any other.

Many thanks to Oleg Molchanov whose YouTube course helped a lot in creating this project.


-- Features --

What you can:

- create simple posts (as admin)
- add tags to the posts (as admin)
- use HTML code to attach images, links, text formatting to the posts
- search posts by keywords
- search posts by tag
- copy link to the post to share
- login as admin to edit/delete posts and tags
- login as owner to create/delete more admin accounts

What you can NOT:

- upload images to the posts
- make text formatting in posts, other than typing HTML code manually
- add tags on post creation/edition page (you can only use admin section for that)
- see the list of all tags


!!!--IMPORTANT--!!!

When deploying on a server, you have to use a command-line to create at least one user account, create and assign to that account roles named "owner" and "admin". After deploying, this user can login and manage users and roles normally via admin section.

Of course, don't forget to edit config.py before deployment.


-- Requirements --

Except Flask itself, the script requires some other packages. Sorry for not providing a normal list of those. Here's my "pip freeze" of required packages and its dependencies (at least, you can be sure there's nothing excess):

alembic==1.7.6

Babel==2.9.1

bcrypt==3.2.0

blinker==1.4

cffi==1.15.0

click==8.0.4

colorama==0.4.4

dnspython==2.2.1

email-validator==1.1.3

Flask==2.0.3

Flask-Admin==1.6.0

Flask-BabelEx==0.9.4

Flask-Login==0.5.0

Flask-Mail==0.9.1

Flask-Migrate==3.1.0

Flask-Principal==0.4.0

Flask-Security==3.0.0

Flask-SQLAlchemy==2.5.1

Flask-WTF==1.0.0

greenlet==1.1.2

idna==3.3

importlib-metadata==4.11.2

importlib-resources==5.4.0

itsdangerous==2.1.0

Jinja2==3.0.3

Mako==1.1.6

MarkupSafe==2.1.0

mysql-connector-python==8.0.28

passlib==1.7.4

pycparser==2.21

pytz==2021.3

six==1.16.0

speaklater==1.3

SQLAlchemy==1.4.32

Werkzeug==2.0.3

WTForms==3.0.1

zipp==3.7.0
