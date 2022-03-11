from wtforms import Form
from wtforms import StringField
from wtforms import TextAreaField


class PostForm(Form):
    title = StringField('Заголовок')
    body = TextAreaField('Текст')
