from fastapi import Depends
from core.core_dep.db_dep import DBDependency

from database.models import User


class UserManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = User