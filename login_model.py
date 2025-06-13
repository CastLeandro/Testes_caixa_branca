from pydantic import BaseModel, EmailStr, field_validator
import re

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def password_strong(cls, value):
        if len(value) < 8:
            raise ValueError("A senha deve ter no mínimo 8 caracteres.")
        if not re.search(r"[A-Z]", value):
            raise ValueError("A senha deve conter ao menos uma letra maiúscula.")
        if not re.search(r"[0-9]", value):
            raise ValueError("A senha deve conter ao menos um número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("A senha deve conter ao menos um caractere especial.")
        return value
