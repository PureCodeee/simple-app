from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class CreateUser(BaseModel):
    name: str


class UsersResponse(BaseModel):
    users: list[User]


users: list[User] = [
    User(id=1, name="genesis_user")
]