from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserSchema(UserPublic):
    password: str


class UserDB(UserSchema):
    id: int


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserResponse]
