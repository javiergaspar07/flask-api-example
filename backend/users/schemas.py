from backend.utilities.fields import UUIDType
from backend.users.db.db_controllers import UserDbController
from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from backend.utilities import Hasher

PASSWORD_REGEX = "^(?=.*?[0-9])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$"


class SignupRequest(BaseModel):
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=25,
    )
    last_name: str = Field(
        ...,
        min_length=2,
        max_length=25,
    )
    email: EmailStr
    password: str = Field(
        regex=PASSWORD_REGEX,
        min_length=8,
        max_length=16,
    )
    password_confirmation: str = Field(
        regex=PASSWORD_REGEX,
        min_length=8,
        max_length=16,
    )

    @validator('password_confirmation')
    def validate_password(cls, password_confirmation, values):
        if not password_confirmation == values.get('password'):
            raise ValueError("Passwords do not match")
        return password_confirmation
    
class SignupResponse(BaseModel):
    id: UUIDType
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=25,
    )
    last_name: str = Field(
        ...,
        min_length=2,
        max_length=25,
    )
    email: EmailStr

    class Config():
        orm_mode = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        regex=PASSWORD_REGEX,
        min_length=8,
        max_length=16,
    )
    context: dict = {}

    @root_validator
    def validate_email(cls, values):
        email = values.get('email')
        if not email:
            ValueError("email parameter needed to perform this action")

        user = UserDbController().get(email=email).one_or_none()
        if not user:
            raise ValueError(f'Wrong username or password')
    
        hashed_password = user.password
        if not Hasher.verify_password(values.get('password'), hashed_password):
            raise ValueError('Wrong username or password')

        values['context'] = {'user': user}
        return values

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str