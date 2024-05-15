from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions.custom_exceptions import UserNotFoundException
from models.core import Salary, User
from models.schemas import SalaryCreate


def create_salary(db: Session, user_id: int, salary_data: SalaryCreate):
    user = db.scalar(select(User).where(User.id == user_id))
    if not user:
        raise UserNotFoundException

    salary = Salary(
        user_id=user_id,
        amount=salary_data.amount,
        next_raise_date=salary_data.next_raise_date
    )
    db.add(salary)
    db.commit()
    return salary


def get_salaries(db: Session, user_id: int):
    return db.scalars(select(Salary).where(Salary.user_id == user_id)).all()
