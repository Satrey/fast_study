from fastapi import APIRouter, Depends  
from starlette import status  

from apps.auth.schemas import RegisterUser, UserReturnData  
from apps.auth.services import UserService  

auth_router = APIRouter(prefix="/auth", tags=["auth"])  

@auth_router.post(
    "/register", 
    response_model=UserReturnData, 
    status_code=status.HTTP_201_CREATED
)  
async def registration(
    user: RegisterUser, 
    service: UserService = Depends(UserService)
) -> UserReturnData:  
    return await service.register_user(user=user)