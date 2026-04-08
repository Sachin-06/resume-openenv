from env import ResumeEnv
from grader import grade

def run_test():
    env = ResumeEnv()

    levels = ["easy", "medium", "hard"]

    for level in levels:
        print("\n==========================")
        print("LEVEL:", level.upper())

        obs = env.reset(level)

        action = "shortlist"

        obs, reward, done, info = env.step(action)

        grade_score = grade(obs, action)

        print("Reward:", reward)
        print("Grade:", grade_score)

if __name__ == "__main__":
    run_test()