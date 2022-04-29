from sqlalchemy.orm import Session
from db.models.users import Blog
from pydantic_schema.schema_blog import BlogCreate

#======================================================================
## --------------------------- return all blogs------------------------
#======================================================================

def get_blogs(db:Session, skip:int=0, limit:int=100):
    return db.query(Blog).offset(skip).limit(limit).all()

#======================================================================
## --------------------------- return one  blog by id:-----------------
#======================================================================

def get_blog_by_id(db:Session,blog_id:int):
    return db.query(Blog).filter(Blog.id == blog_id).first()


#======================================================================
## --------------------------- create a blog and return blogs created------------------------
#======================================================================

def create_blog(db:Session, blog:BlogCreate):
    db_blog = Blog(title = blog.title, description = blog.description, user_id = blog.user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog