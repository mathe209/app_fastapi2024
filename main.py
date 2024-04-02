from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

import models, Schemas
import models
import dataabases
from dataabases import SessionLocal, engine
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
# Dependency creation
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/test_get") #the data will be displayed on the font end app when the user uses the GET operation
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts
    #returning a post with a specific id number
    #posts = db.query(models.Post).filter(models.Post.id==1).fist()

@app.post("/create_post", response_model= Schemas.ResponseData)
def create_entry(post: Schemas.PostBase, db: Session = Depends(get_db)):
    print(post.dict()) #converting the pydantic model to a dictionary
    #ensures that i dont have to write out all the fields when creating a post even if i enter a new field
    entry = models.Post(**post.dict())
    #entry = models.Post(title=post.title, content=post.content)
    db.add(entry)
    db.commit()
    #db.refresh(entry) #displays the created post on the app

    return entry

@app.get("/post/{id}")
def get_by_id(id:int, db: Session = Depends(get_db)):
    #uses the {id} value provided by the user
    posts = db.query(models.Post).filter(models.Post.id==id).first()

    if posts is None:
        raise HTTPException(status_code=404, detail=f"The post with id {id} does not exist!")
    
    return {posts}

@app.delete("/delete/{id}", status_code=204)
def delete_post(id: int, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id==id)
    posts.delete()
    db.commit()

    if posts is None:
        raise HTTPException(status_code=404, detail=f"The post with id {id} does not exist!")
    return Response(status_code=404)

@app.put("/update_post/{id}")
def update_post(id:int,post:Schemas.PostUpdate, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id==id)
    posts.update(post.dict())

    if posts.first() is None:
        raise HTTPException(status_code=404, detail=f"The post with id {id} does not exist!")
    
    db.commit()
    return {"Successful update"}