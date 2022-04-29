from datetime import datetime
from pydantic import  BaseModel


class LikeBase(BaseModel):
    user_id : int
    blog_id : int
class LikeCreate(LikeBase):
    ...
class Like(LikeBase):
    created_at : datetime
    updated_at : datetime