from datetime import datetime
from pydantic import  BaseModel

class CommentBase(BaseModel):
    description : str
    user_id : int
    blog_id : int
class CommentCreate(CommentBase):
    ...
class Comment(CommentBase):
    id : int
    created_at : datetime
    updated_at : datetime