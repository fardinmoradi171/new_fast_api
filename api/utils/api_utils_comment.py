from sqlalchemy.orm import Session
from db.models.users import Comment
from pydantic_schema.schema_comment import CommentCreate



def get_comment(db:Session, comment_id:int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comments(db:Session,blog_id:int,skip:int=0,limit:int=100):
    return db.query(Comment).filter(Comment.blog_id == blog_id).offset(skip).limit(limit).all()

def create_comment(db:Session,comment:CommentCreate):
    db_comment = Comment(
        description=comment.description,
        blog_id = comment.blog_id,
        user_id = comment.user_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment