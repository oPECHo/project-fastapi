from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    return {'data': f'{limit} blogs from the db'}
    
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'date': id }


@app.get('/blog/{id}/comment')
def comments(id, limit = 10):
    # fetch comment of blog with id = id
    return {'date': {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is create with title as {blog.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=3000)