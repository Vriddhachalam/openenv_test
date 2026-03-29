import random
from models import Email, Observation, Action
from tasks import get_task 

class EmailEnv:
    def __init__(self, task_name="easy"):
        self.task_name = task_name  # ← THIS LINE (the missing brain cell)
        self.emails = []
        self.processed = []
        self.done = False

    def reset(self):
        # self.emails = [
        #     Email(subject="Win money!!!", body="Click now", label="spam"),
        #     Email(subject="Project deadline", body="Due tomorrow", label="important"),
        #     Email(subject="Lunch?", body="Shall we?", label="normal"),
        # ]
        raw_emails = get_task(self.task_name)
    
        self.emails = [
            Email(subject=e["subject"], body="", label=e["label"])
            for e in raw_emails
        ]
        self.processed = []
        self.done = False
        return self.state()

    def state(self):
        return Observation(
            inbox=self.emails,
            processed=self.processed
        )

    def step(self, action: Action):
        if self.done:
            return self.state(), 0.0, True, {}

        email = self.emails[action.email_index]
        reward = 0

        # reward logic
        if action.action_type == "mark_spam" and email.label == "spam":
            reward = 1
        elif action.action_type == "mark_important" and email.label == "important":
            reward = 1
        elif action.action_type == "skip":
            reward = 0
        else:
            reward = -1  # wrong action

        self.processed.append(email.subject)
        self.emails.pop(action.email_index)

        if len(self.emails) == 0:
            self.done = True

        return self.state(), reward, self.done, {}