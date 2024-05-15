from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

from controllers.salaries import create_salary, get_salaries
from models import schemas
from models.database import get_db
from secure import apikey_scheme
from views.users import get_user_by_token

router = APIRouter()


@router.post("", response_model=schemas.Salary, status_code=201)
def add_salary(
    salary_data: schemas.SalaryCreate,
    access_token: Annotated[str, Depends(apikey_scheme)],
    db: Session = Depends(get_db)
):
    user = get_user_by_token(access_token=access_token, db=db)
    return create_salary(db=db, user_id=user["id"], salary_data=salary_data)


@router.get("", response_model=List[schemas.Salary])
def read_salaries(
    access_token: Annotated[str, Depends(apikey_scheme)],
    db: Session = Depends(get_db)
):
    user = get_user_by_token(access_token=access_token, db=db)
    return get_salaries(db=db, user_id=user["id"])
