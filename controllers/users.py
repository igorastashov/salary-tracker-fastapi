from sqlalchemy import select
from sqlalchemy.orm import Session

from models.core import User
from models.schemas import UserCreate
from secure import pwd_context
from exceptions.custom_exceptions import UserAlreadyExistsException


def register(db: Session, user_data: UserCreate):
    if db.scalar(select(User).where(User.email == user_data.email)):
        raise UserAlreadyExistsException()
    user = User(email=user_data.email)
    user.hashed_password = pwd_context.hash(user_data.password)
    db.add(user)
    db.commit()
    return {
        "id": user.id,
        "email": user.email,
    }
