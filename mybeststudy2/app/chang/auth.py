from app.chang import chang
from app.models.topic import Topic
from app.models.users import Users
from flask_login import login_required
from app.models.base import db

@chang.route('/hello')

def hello():
    with db.auto_commit():

        a = Users()
        b =Topic()



        db.session.add(b)
        a.email="1213s21aa2"
        a.password="12211121"
        db.session.add(a)

    return "嘻嘻嘻"