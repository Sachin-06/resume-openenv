from pydantic import BaseModel
from typing import List

class Action(BaseModel):
    resume: str
    job_description: str

class Observation(BaseModel):
    matched_skills: List[str]
    missing_skills: List[str]

class Reward(BaseModel):
    score: float