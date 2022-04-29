from fastapi import FastAPI
from db.db_setup import engine
from api import api_user,api_blog
from db.models import users



users.Base.metadata.create_all(bind=engine)


 
app = FastAPI()


app.include_router(api_user.router)
app.include_router(api_blog.router)