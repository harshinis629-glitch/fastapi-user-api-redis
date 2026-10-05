from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int

    class Config:
        from_attributes = True