"""
Database set-up script for item catalogue
"""

# [START Imports]
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
# [END Imports]

Base = declarative_base()


class User(Base):
    """
    Table to store User information
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    """
    Table to store categories used to classify the books
    Inputs required category_name
    Category_id is autogenerated
    """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Book(Base):
    """
    Table to store books
    Inputs required book_name; and foreign key = category_name
    Inputs optional book_description, book_author, book_price
    Book_id is autogenerated
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(750))
    author = Column(String(250))
    price = Column(String(8))
    created_at = Column(DateTime, default=datetime.now())
    updated_up = Column(DateTime, onupdate=datetime.now())
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


engine = create_engine('sqlite:///cataloguebooksv2.db')

Base.metadata.create_all(engine)
