from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.users import register
from models import schemas
from models.database import get_db
from secure import apikey_scheme
from views.users import get_user_by_token, get_users

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.User],
    tags=["2. Получить список всех пользователей"],
)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post(
    "",
    response_model=schemas.LiteUser,
    status_code=201,
    tags=["3. Зарегистрировать нового пользователя"],
)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)


@router.get(
    "/self",
    response_model=schemas.LiteUser,
    tags=["4. Получить информацию о текущем пользователе по токену"],
)
def get_user_by_id(
    access_token: Annotated[str, Depends(apikey_scheme)], db: Session = Depends(get_db)
):
    return get_user_by_token(access_token=access_token, db=db)
