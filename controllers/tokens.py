import uuid
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from exceptions.custom_exceptions import (
    IncorrectCredentialsException,
    UserNotFoundException,
)
from models.core import Token, User
from models.schemas import UserAuth
from secure import pwd_context

# Время жизни токена в минутах
TOKEN_EXPIRE_MINUTES = 1


def create_token(db: Session, user_data: UserAuth):
    # Получим пользователя по email с его проверкой
    user: User = db.scalar(select(User).where(User.email == user_data.email))
    if not user:
        raise UserNotFoundException()

    # Проверим пароль
    if not pwd_context.verify(user_data.password, user.hashed_password):
        raise IncorrectCredentialsException()

    # Удалим существующий токен, если он есть
    existing_token = db.scalar(select(Token).where(Token.user_id == user.id))
    if existing_token:
        db.delete(existing_token)
        db.commit()

    # Создадим новый токен
    expires_at = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    token: Token = Token(
        user_id=user.id, access_token=str(uuid.uuid4()), expires_at=expires_at
    )
    db.add(token)
    db.commit()
    db.refresh(token)  # Обновим объект токена после коммита

    return {"access_token": token.access_token, "expires_at": token.expires_at}
