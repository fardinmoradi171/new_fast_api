from ctypes.wintypes import CHAR
import enum
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String,Enum,Text
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixin import Timestamp

class Role(enum.IntEnum):
    admin = 1
    staff = 2
    user = 3
class User(Timestamp,Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(100),unique=True,index=True, nullable=True)
    # password = Column(String(50),min_length=8,nullable=True,)
    password = Column(String,nullable=True)
    is_active = Column(Boolean,default=False)
    role = Column(Enum(Role))
    # relationship:
    user_blog = relationship("Blog", back_populates="blog_user")
    user_comment = relationship("Comment", back_populates="comment_user")
    user_like = relationship("Like", back_populates="like_user")
    
class Blog(Timestamp,Base):
    __tablename__ = "blogs"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    description = Column(Text,nullable=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    #relationship:
    blog_user = relationship("User", back_populates="user_blog")
    blog_comment = relationship("Comment", back_populates="comment_blog")
    blog_like = relationship("Like", back_populates="like_blog")

class Comment(Timestamp,Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True,index=True)
    description = Column(Text,nullable=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    blog_id = Column(Integer,ForeignKey("blogs.id"))
    #relationship:
    comment_user = relationship("User", back_populates="user_comment")
    comment_blog = relationship("Blog", back_populates="blog_comment")
      
class Like(Timestamp,Base):
    __tablename__ = "likes"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    blog_id = Column(Integer,ForeignKey("blogs.id"))
    # relationship:
    like_user = relationship("User", back_populates="user_like")
    like_blog = relationship("Blog", back_populates="blog_like")
    
    