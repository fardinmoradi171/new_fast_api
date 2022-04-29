from datetime import datetime
from pydantic import  BaseModel




class BlogBase(BaseModel):
    title : str
    description : str
    user_id : int
class BlogCreate(BlogBase):
    ...
class Blog(BlogBase):
    id : int
    created_at : datetime
    updated_at : datetime



   