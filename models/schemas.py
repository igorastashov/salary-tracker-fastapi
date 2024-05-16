from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


UserAuth = UserCreate


class LiteUser(UserBase):
    id: int


class User(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    expires_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SalaryBase(BaseModel):
    amount: int
    next_raise_date: datetime


class SalaryCreate(SalaryBase):
    pass


class Salary(SalaryBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
