import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from login_model import LoginRequest

def test_senha_apenas_numeros():
    with pytest.raises(ValueError):
        LoginRequest(email="user@exemplo.com", password="123")

def test_senha_letras_minusculas():
    with pytest.raises(ValueError):
        LoginRequest(email="user@exemplo.com", password="abcd123")

def test_senha_sem_especial():
    with pytest.raises(ValueError):
        LoginRequest(email="user@exemplo.com", password="Senha1223")

def test_senha_curta():
    with pytest.raises(ValueError):
        LoginRequest(email="user@exemplo.com", password="Se1#")

def test_email_invalido():
    with pytest.raises(ValueError):
        LoginRequest(email= "user.com", password="senhaForte@123")

def test_login_valido():
    login = LoginRequest(email="user@exemplo.com", password="SenhaForte@123")
    assert login.password == "SenhaForte@123"
    assert login.email == "user@exemplo.com"
