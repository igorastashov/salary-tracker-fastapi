from fastapi.security import APIKeyHeader
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')
apikey_scheme = APIKeyHeader(name="Authorization")
