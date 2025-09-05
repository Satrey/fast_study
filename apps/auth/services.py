from fastapi import Depends  

from apps.auth.handlers import AuthHandler  
from apps.auth.managers import UserManager  
from apps.auth.schemas import RegisterUser, UserReturnData, CreateUser  


class UserService:  
    def __init__(self, manager: UserManager = Depends(UserManager), handler: AuthHandler = Depends(AuthHandler)):  
        self.manager = manager  
        self.handler = handler  

    async def register_user(self, user: RegisterUser) -> UserReturnData:  
        hashed_password = await self.handler.get_password_hash(user.password)  

        new_user = CreateUser(email=user.email, hashed_password=hashed_password)  

        return await self.manager.create_user(user=new_user)