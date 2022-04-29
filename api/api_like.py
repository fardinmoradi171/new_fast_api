import fastapi
from pydantic_schema.schema_like import Like,LikeCreate
from db.db_setup import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.utils.api_utils_blog import (get_likes,create_like)




router = fastapi.APIRouter()


@router.get("/blogs/likes")
async def read_likes(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    likes = get_likes(db=db,skip=skip,limit=limit)
    return likes

@router.post("/blogs/addlike")
async def create_new_like(like:LikeCreate, db:Session=Depends(get_db)):
    return create_like(db=db, like=like)