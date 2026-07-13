from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class CreateUser(BaseModel):
    name: str


class UsersResponse(BaseModel):
    users: list[User]


DEFAULT_USERS = [
    User(id=1, name="genesis_user"),
]


users = DEFAULT_USERS.copy()