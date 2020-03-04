from config import engine
from config import metadata
from config import app
import uvicorn

from post.route import post_route

app.include_router(post_route, prefix="/api/post", tags=["post"])


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD Example."}


if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

