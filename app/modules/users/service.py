from sqlalchemy.orm import Session
from .schemas import UserSignUp
from .repository import UserRepository
from passlib.context import CryptContext
from utils.jwt_handler import create_access_token
from utils.security import verify_password
from utils.email import send_welcome_email  

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def get_users(self):
        return self.repo.get_all_users()

    def get_user_id(self, user_id: int):
        user = self.repo.get_user_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def login(self, email: str, password: str):
        user = self.repo.get_user_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.password):
            raise ValueError("Invalid credentials")

        token = create_access_token({
            "user_id": user.id,
            "email": user.email
        })

        return {"access_token": token, "token_type": "bearer"}
    
    def create(self, data: UserSignUp):
        existing = self.repo.get_user_by_email(data.email)
        if existing:
            raise ValueError("Email already registered")

        truncated_password = data.password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
        data.password = pwd_context.hash(truncated_password)

        user = self.repo.create(data)
        send_welcome_email(user.email, user.fullname)

        return user
    