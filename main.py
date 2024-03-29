from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import models
import dataabases
from dataabases import SessionLocal, engine
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""create a schema so that the data is validated"""
"""the class defines the schema and how the code looks like"""
"""the user must send the title as a string and the content of the post"""
class Post(BaseModel):
    title: str
    content: str
    published: bool = True #this is a default field
    rating: Optional[int] = None


@app.get("/test_get") #the data will be displayed on the font end app when the user uses the GET operation
def get_post(schema: Post, db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    #returning a post with a specific id number
    #posts = db.query(models.Post).filter(models.Post.id==1).fist()

@app.post("/create_post")
def create_entry(post: Post, db: Session = Depends(get_db)):
    entry = models.Post(title=post.title, content=post.content)
    db.add(entry)
    db.commit()
    #db.refresh(entry) #retreiving the created post

    return {"data": entry}
    
