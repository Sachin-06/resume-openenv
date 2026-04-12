from models import Action

SKILLS = ["python", "ml", "docker", "aws", "sql", "kubernetes"]

class ResumeEnv:
    def __init__(self):
        self.done = False
        self.task = "easy"

    def reset(self, task="easy"):
        self.done = False
        self.task = task
        return {"message": f"Environment reset for {task} task"}

    def state(self):
        return {"done": self.done, "task": self.task}

    def extract(self, text):
        text = text.lower()
        return [s for s in SKILLS if s in text]

    def step(self, action: Action):
        resume_skills = self.extract(action.resume)
        job_skills = self.extract(action.job_description)

        matched = list(set(resume_skills) & set(job_skills))
        missing = list(set(job_skills) - set(resume_skills))

        base_score = len(matched) / len(job_skills) if job_skills else 0.0

        from grader import grade
        final_score = grade(self.task, base_score)

        self.done = True

        return {
            "observation": {
                "matched_skills": matched,
                "missing_skills": missing
            },
            "reward": final_score,
            "done": self.done,
            "info": {"task": self.task}
        }