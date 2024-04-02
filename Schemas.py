from pydantic import BaseModel

"""create a schema so that the data is validated"""
"""the class defines the schema and how the code looks like"""
"""the user must send the title as a string and the content of the post"""
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True #this is a default field
    time_of_day: str
    #rating: Optional[int] = None

class PostUpdate(BaseModel):
    title: str
    content: str

#adding a schema to describe the shape of the response
class ResponseData(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True
