from services.database.base import BaseModel, db, PydanticBaseModel


class RuleSchema(PydanticBaseModel):
    user_id:str
    tag_name:str
    words: list[str]

class Rule(BaseModel):
    scheme = db.tag_rules
    validation = RuleSchema