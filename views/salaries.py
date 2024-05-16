from sqlalchemy.orm import Session
from sqlalchemy import select

from models.core import Salary


def get_salaries(db: Session, user_id: int):
    return db.scalars(select(Salary).where(Salary.user_id == user_id)).all()
