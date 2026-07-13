from fastapi import APIRouter
from app.models import users

router = APIRouter(prefix="/api/users")


@router.get("/")
async def get_users():
    return {"users": users}