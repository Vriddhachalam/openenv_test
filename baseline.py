from environment import EmailEnv
from models import Action

env = EmailEnv()
obs = env.reset()

total_reward = 0

while True:
    if not obs.inbox:
        break

    email = obs.inbox[0]

    # simple rule-based agent
    if "Win" in email.subject or "Free" in email.subject:
        action = Action(action_type="mark_spam", email_index=0)
    elif "Urgent" in email.subject or "deadline" in email.subject:
        action = Action(action_type="mark_important", email_index=0)
    else:
        action = Action(action_type="skip", email_index=0)

    obs, reward, done, _ = env.step(action)
    total_reward += reward
    print("\n--- STEP ---")
    print("Inbox:", [e.subject for e in obs.inbox])
    print("Action:", action)
    print("Reward:", reward)
    if done:
        break

print("Total Reward:", total_reward)