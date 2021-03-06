from flask import Flask
from flask import request
from flask import redirect
from flask import url_for

from flask_sqlalchemy import SQLAlchemy

from config import Configuration

from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


# importing here to avoid circular import exception
from models import Post, Tag, User, Role


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class OwnerMixin:
    def is_accessible(self):
        return current_user.has_role('owner')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


class UserRoleView(OwnerMixin, BaseModelView):
    pass


admin = Admin(app, 'Вернуться', url='/', index_view=HomeAdminView(name='Выберите -->'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(UserRoleView(User, db.session))
admin.add_view(UserRoleView(Role, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
