from fastapi import FastAPI, HTTPException
from login_model import LoginRequest
import uvicorn
app = FastAPI()

@app.post("/login")
def login(request: LoginRequest):
    fake_user = {
        "email": "user@example.com",
        "password": "SenhaForte@123"
    }

    if request.email != fake_user["email"] or request.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {"message": "Login realizado com sucesso"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")