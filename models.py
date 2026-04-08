from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    candidate_skills: List[str]
    experience: int
    job_required_skills: List[str]