from fastapi import APIRouter, status
from app.models import UsersResponse, users, CreateUser, User


router = APIRouter(prefix="/api/users")


@router.get("/", response_model=UsersResponse)
async def get_users():
    return {"users": users}


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser):
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, name=user.name)
    users.append(new_user)
    return new_user