import fastapi
from pydantic_schema.schema_user import UserCreate,User
from db.db_setup import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.utils.api_utils_user import (
    get_user,
    get_user_by_email,
    get_users,
    create_user
    )


router = fastapi.APIRouter()


@router.get("/users")
async def read_users(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    users = get_users(db,skip=skip,limit=limit)
    return users
   

@router.post("/users")
async def create_new_user(user:UserCreate, db:Session=Depends(get_db)):
    return create_user(db=db, user=user)