from pydantic import BaseModel
from typing import List

class Email(BaseModel):
    subject: str
    body: str
    label: str  # "spam", "important", "normal"

class Observation(BaseModel):
    inbox: List[Email]
    processed: List[str]

class Action(BaseModel):
    action_type: str  # "mark_spam", "mark_important", "skip"
    email_index: int

class Reward(BaseModel):
    value: float