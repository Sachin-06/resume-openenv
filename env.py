from models import Action, Observation, Reward

SKILLS = ["python", "ml", "docker", "aws", "sql"]

class ResumeEnv:
    def __init__(self):
        self.done = False

    def reset(self):
        self.done = False
        return {"message": "Environment reset"}

    def state(self):
        return {"done": self.done}

    def extract(self, text):
        text = text.lower()
        return [s for s in SKILLS if s in text]

    def step(self, action: Action):
        resume_skills = self.extract(action.resume)
        job_skills = self.extract(action.job_description)

        matched = list(set(resume_skills) & set(job_skills))
        missing = list(set(job_skills) - set(resume_skills))

        score = len(matched) / len(job_skills) if job_skills else 0.0

        self.done = True

        return {
            "observation": {
                "matched_skills": matched,
                "missing_skills": missing
            },
            "reward": score,
            "done": self.done,
            "info": {}
        }