import logging
import sys

from fastapi import APIRouter, Depends, status, HTTPException
from .shcemas import UserCreate, UserRead
from src.db.postgres.session import get_db
from src.models.user import User

from src.core.security import get_password_hash

router = APIRouter()

@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Создание нового пользователя",
    description="Регистрация пользователя по email и паролю",
)
async def create_user(
        user_data: UserCreate,
        db=Depends(get_db),
):
    hashed_password = get_password_hash(str(user_data.password.get_secret_value()))
    print("Hashed password: ", hashed_password, file=sys.stderr)
    print("Hashed password: ", hashed_password, file=sys.stderr)
    if db.query(User).filter(User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # чтобы подгрузить created_at
    return UserRead.model_validate(db_user)
