from flask import session
from datetime import  datetime, timedelta
from services.database.base import BaseModel, db, PydanticBaseModel

class UserSchema(PydanticBaseModel):

    login: str
    password: str
    bot_token: str

class User(BaseModel):
    scheme = db.users
    validation = UserSchema

    @staticmethod
    def create_session(login:str, user_id:str):
        session.update({
            'login':login,
            'user_id':user_id,
            'created_at': datetime.now().timestamp(),
            'life_time': (datetime.now() + timedelta(hours=1)).timestamp()})

    @staticmethod
    def update_session_lifetime():
        session['life_time'] = (datetime.now() + timedelta(hours=1)).timestamp()

    @staticmethod
    def close_session():
        session.clear()

    @staticmethod
    def is_valid():
        if not session:
            return False
        if session['life_time'] < datetime.now().timestamp():
            return

        return  True

    @staticmethod
    def login():
        return session['login']

    @staticmethod
    def id():
        return session['user_id']