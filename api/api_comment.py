import fastapi
from pydantic_schema.schema_comment import Comment,CommentCreate
from db.db_setup import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.utils.api_utils_blog import (get_comments,get_comment,create_comment)



router = fastapi.APIRouter()


@router.get("/blogs/comments")
async def read_comments(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    comments = get_comments(db=db,skip=skip,limit=limit)
    return comments

@router.post("/blogs/addcomments")
async def create_new_comment(comment:CommentCreate, db:Session=Depends(get_db)):
    return create_comment(db=db, comment=comment)