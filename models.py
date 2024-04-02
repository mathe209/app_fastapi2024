from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#sqlalchemy doesnt allow for automatic modification of tables, so delete the table first to make updates

#the post model is used to query, and talk with the database
class Post(Base):
    __tablename__ = "posts_2024"
    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    time_of_day = Column(String, nullable=False)
    published = Column(Boolean,server_default="True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))



