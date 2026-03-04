import random

knowledge_base = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm functioning well.", "Doing great!", "All systems operational."],
    "name": ["I prefer to stay anonymous.", "Names are just labels."],
    "weather": ["Weather depends on your location.", "It seems pleasant today."],
}

default_responses = [
    "Interesting question.",
    "Can you elaborate?",
    "That depends on perspective.",
    "Why do you ask?"
]

def ai_response(question):
    question = question.lower()
    for key in knowledge_base:
        if key in question:
            return random.choice(knowledge_base[key])
    return random.choice(default_responses)