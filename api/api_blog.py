import fastapi
from pydantic_schema.schema_blog import Blog,BlogCreate
from db.db_setup import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.utils.api_utils_blog import (get_blogs,get_blog_by_id,create_blog)

router = fastapi.APIRouter()


@router.get("/blogs")
async def read_blogs(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    blogs = get_blogs(db=db,skip=skip,limit=limit)
    return blogs

@router.post("/blogs")
async def create_new_blog(blog:BlogCreate, db:Session=Depends(get_db)):
    return create_blog(db=db, blog=blog)
