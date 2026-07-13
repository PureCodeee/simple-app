from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

users = [
    User(id=1, name="genesis_user")
]