from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int
    fname: str
    lname: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
