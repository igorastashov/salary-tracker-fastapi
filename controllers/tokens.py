import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from starlette.status import HTTP_404_NOT_FOUND

from models.core import User, Token
from models.schemas import UserAuth
from secure import pwd_context


def create_token(db: Session, user_data: UserAuth):
    user: User = db.scalar(select(User).where(User.email == user_data.email))
    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not pwd_context.verify(user_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token: Token = Token(user_id=user.id, access_token=str(uuid.uuid4()))
    db.add(token)
    db.commit()
    return {
        "access_token": token.access_token
    }

