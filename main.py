from env import ResumeEnv

env = ResumeEnv()

obs = env.reset()
print("Initial Observation:", obs)

obs, reward, done, info = env.step("shortlist")

print("Reward:", reward)
print("Done:", done)
print("Info:", info)