from sqlalchemy.orm import Session
from .schemas import UserSignUp
from .repository import UserRepository
from passlib.context import CryptContext
from utils.jwt_handler import create_access_token
from utils.security import verify_password

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
        # 1. Find user by email
        user = self.repo.get_user_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        # 2. Verify password
        if not verify_password(password, user.password):
            raise ValueError("Invalid credentials")

        # 3. Create token
        token = create_access_token({
            "user_id": user.id,
            "email": user.email
        })

        return {"access_token": token, "token_type": "bearer"}

    def create(self, data: UserSignUp):
        truncated_password = data.password.encode("utf-8")[:72].decode("utf-8", errors="ignore")
        data.password = pwd_context.hash(truncated_password)
        return self.repo.create(data)