# tasks.py

def get_task(task_name):
    if task_name == "easy":
        return [
            {"subject": "Win money!!!", "label": "spam"},
            {"subject": "Meeting today", "label": "important"},
        ]

    elif task_name == "medium":
        return [
            {"subject": "Free vacation", "label": "spam"},
            {"subject": "Client update", "label": "important"},
            {"subject": "Random chat", "label": "normal"},
        ]

    elif task_name == "hard":
        return [
            {"subject": "Urgent: account issue", "label": "important"},
            {"subject": "You won lottery", "label": "spam"},
            {"subject": "Follow up", "label": "normal"},
            {"subject": "Security alert", "label": "important"},
        ]

    else:
        raise ValueError("Unknown task")