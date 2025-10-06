from pydantic import BaseModel, Field, EmailStr, ConfigDict


# Добавили описание структуры пользователя
class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")  # Использовали alise
    first_name: str = Field(alias="firstName")  # Использовали alise
    middle_name: str = Field(alias="middleName")  # Использовали alise
    phone_number: str = Field(alias="phoneNumber")  # Использовали alise


# Добавили описание структуры ответа получения пользователя
class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных для создания нового пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")  # Использовали alise
    first_name: str = Field(alias="firstName")  # Использовали alise
    middle_name: str = Field(alias="middleName")  # Использовали alise
    phone_number: str = Field(alias="phoneNumber")  # Использовали alise


# Добавили описание структуры ответа создания пользователя
class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema