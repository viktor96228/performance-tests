from pydantic import BaseModel, Field, EmailStr

# модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

# модель CreateUserRequestSchema
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

# модель CreateUserRequestSchema
class CreateUserResponseSchema(BaseModel):
    user: list[UserSchema]

