from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from exceptions.custom_exceptions import UnauthorizedException, ExpiredTokenException

from models import core
from models.core import Token


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(core.User).offset(skip).limit(limit).all()


def get_user_by_token(access_token: str, db: Session):
    token = db.scalar(select(Token).where(Token.access_token == access_token))
    if token:
        if token.expires_at < datetime.utcnow():
            raise ExpiredTokenException()
        return {
            "id": token.user.id,
            "email": token.user.email
        }
    else:
        raise UnauthorizedException()
