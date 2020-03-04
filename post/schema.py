from datetime import datetime
from pydantic import BaseModel


''' Model Schema Using Pydantic '''


class Post(BaseModel):
    id: int
    title: str
    body: str
    is_published: bool = False  # Providing a default value False
    created: datetime = datetime.utcnow()
    modified: datetime = datetime.utcnow()
