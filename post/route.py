from fastapi import APIRouter
from typing import List
from config import database
import secrets

from .model import posts
from .schema import Post

post_route = APIRouter()


@post_route.get("/posts", response_model=List[Post], status_code=200)
async def all_posts():
    query = posts.select()
    all_posts = await database.fetch_all(query)
    if posts is None:
        return {"message": " No post found!"}
    else:
        return all_posts


@post_route.get("/post/{id}", response_model=Post, status_code=200)
async def get_post(id:int):
    query = posts.select().where(posts.c.id == id)
    return await database.fetch_one(query=query)


@post_route.post("/create/", response_model=Post, status_code=201)
async def create(post: Post):
    query = posts.insert().values(title=post.title, body=post.body, is_published=post.is_published,
                                  created=post.created, modified=post.modified)
    last_record_id = await database.execute(query=query)
    return {**post.dict(), "id": last_record_id}


@post_route.patch("/update/{id}", response_model=Post)
async def update(id:int, post: Post):
    query = posts.update().where(posts.c.id == id).values(title=post.title, body=post.body,
                                                          is_published=post.is_published, created=post.created,
                                                          modified=post.modified)
    last_record_id = await database.execute(query=query)
    return {**post.dict(), "id": last_record_id}


@post_route.delete("/delete/{id}", response_model=Post)
async def delete(id:int):
    query = posts.delete().where(posts.c.id == id)
    return await database.execute(query)
