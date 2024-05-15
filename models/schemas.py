from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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
    items: List[Item] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    expires_at: datetime

    class Config:
        orm_mode = True


class SalaryBase(BaseModel):
    amount: int
    next_raise_date: datetime


class SalaryCreate(SalaryBase):
    pass


class Salary(SalaryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
