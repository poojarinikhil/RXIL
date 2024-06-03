from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EntityBase(BaseModel):
    name: str
    description: Optional[str] = None

class EntityCreate(EntityBase):
    user_id: int

class Entity(EntityBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    entities: List[Entity] = []

    class Config:
        orm_mode = True
