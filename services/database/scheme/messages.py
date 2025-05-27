from services.database.base import BaseModel, db, PydanticBaseModel


class MessageSchema(PydanticBaseModel):
    user_id:str
    chat_id:str
    text:str


class Message(BaseModel):
    scheme = db.messages
    validation = MessageSchema