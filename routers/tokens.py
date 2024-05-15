from controllers.tokens import create_token
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import schemas
from models.database import get_db


router = APIRouter()


@router.post("", response_model=schemas.Token, status_code=201)
def create_token_for_user(user_data: schemas.UserAuth, db: Session = Depends(get_db)):
    return create_token(db=db, user_data=user_data)
