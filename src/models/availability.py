from pydantic import BaseModel
from typing import List, Optional, Dict

class Availability(BaseModel):
  preference: Optional[List[str]] = []
  constraints: List[str]

class UserData(BaseModel):
  message: str
  availability: Availability

class Users(BaseModel):
  data: Dict[str, UserData] = {}