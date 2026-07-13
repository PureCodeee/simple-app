from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class CreateUser(BaseModel):
    name: str


users: list[User] = [
    User(id=1, name="genesis_user")
]