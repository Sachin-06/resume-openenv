from env import ResumeEnv
from grader import grade

def simple_agent(obs):
    skills = obs.candidate_skills
    required = obs.job_required_skills

    match = len(set(skills) & set(required)) / len(required)

    if match >= 0.5:
        return "shortlist"
    else:
        return "reject"


def run_agent():
    env = ResumeEnv()
    levels = ["easy", "medium", "hard"]

    total_score = 0

    for level in levels:
        obs = env.reset(level)

        action = simple_agent(obs)

        _, reward, _, _ = env.step(action)
        print("Reward:", reward.score)

        g = grade(obs.model_dump(), action)

        print(f"\nLevel: {level}")
        print("Action:", action)
        print("Reward:", reward.score)
        print("Grade:", g)

        total_score += g

    print("\nFinal Score:", total_score / 3)


if __name__ == "__main__":
    run_agent()