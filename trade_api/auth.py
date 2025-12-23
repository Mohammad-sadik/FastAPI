from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from slowapi import Limiter
from slowapi.util import get_remote_address

from config import settings

# Rate Limiter
limiter = Limiter(key_func=get_remote_address)

# Password hashing
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# In-memory user store
PASSWORD_HASH = pwd_context.hash("secret")

FAKE_USERS_DB = {
    "admin": {
        "username": "admin",
        "password_hash": PASSWORD_HASH,
        "disabled": False,
    }
}


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire, "iat": datetime.utcnow()})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str | None = payload.get("sub")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = FAKE_USERS_DB.get(username)
    if not user:
        raise credentials_exception

    return user
