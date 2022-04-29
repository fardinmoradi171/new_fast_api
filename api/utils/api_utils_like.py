from sqlalchemy.orm import Session
from db.models.users import Like
from pydantic_schema.schema_like import LikeCreate








def get_likes(db:Session,blog_id:int ,skip:int=0,limit:int=100):
    return db.query(Like).filter(Like.blog_id == blog_id).offset(skip).limit(limit).all()

def create_like(db:Session,like:LikeCreate):
    db_like = Like(user_id = like.user_id, blog_id = like.blog_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like