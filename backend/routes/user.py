from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db_connection, get_password_hash, verify_password
from auth import create_access_token
from datetime import timedelta

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register")
async def register(username: str, password: str):
    conn = get_db_connection()
    hashed_password = get_password_hash(password)
    
    try:
        conn.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    except:
        raise HTTPException(status_code=400, detail="Benutzername existiert bereits")
    finally:
        conn.close()
    
    return {"message": "User erfolgreich registriert"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (form_data.username,)).fetchone()
    conn.close()

    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Falsche Login-Daten")

    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}
