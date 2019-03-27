

from sqlalchemy import Column,Integer,String
#上面两个为密码的加密和对比
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base
from flask_login import UserMixin
#从flask——login初始化后的那个地方获得的
from  app.app import login_manager

class Users(Base,UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)


    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)




@login_manager.user_loader
def get_user(uid):
    return Users.query.get(int(uid))
