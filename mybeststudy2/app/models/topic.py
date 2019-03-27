from sqlalchemy import Column,Integer,String

from app.models.base import Base


class Topic(Base):
    id = Column(Integer, primary_key=True)
    topic = Column(String(24),nullable=True)