from fastapi import APIRouter, status
from app.models import users, CreateUser, User


router = APIRouter(prefix="/api/users")


@router.get("/", response_model=list[User])
async def get_users():
    return users


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser):
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, name=user.name)
    users.append(new_user)
    return new_user