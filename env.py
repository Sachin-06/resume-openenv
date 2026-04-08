from models import Observation

class ResumeEnv:

    def __init__(self):
        self.state_data = None

    # MUST NOT take parameters
    def reset(self):
        level = "easy"

        if level == "easy":
            self.state_data = Observation(
                candidate_skills=["python", "ml"],
                experience=3,
                job_required_skills=["python", "ml"]
            )

        elif level == "medium":
            self.state_data = Observation(
                candidate_skills=["python"],
                experience=1,
                job_required_skills=["python", "ml"]
            )

        else:
            self.state_data = Observation(
                candidate_skills=["java"],
                experience=5,
                job_required_skills=["python", "ml"]
            )

        return self.state_data.model_dump()

    def step(self, action):
        skills = self.state_data.candidate_skills
        required = self.state_data.job_required_skills

        matched = len(set(skills) & set(required))
        total = len(required)

        skill_score = matched / total

        experience = self.state_data.experience
        exp_score = min(experience / 5, 1.0)

        reward = 0.7 * skill_score + 0.3 * exp_score

        # penalties
        if action == "reject" and reward > 0.6:
            reward -= 0.5
        elif action == "shortlist" and reward < 0.4:
            reward -= 0.5

        reward = max(0.0, min(1.0, reward))

        done = True

        info = {
            "skill_score": skill_score,
            "experience_score": exp_score
        }

        return self.state_data.model_dump(), float(reward), done, info

    def state(self):
        return self.state_data.model_dump()