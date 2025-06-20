import re
import random

patterns = {
         r'what is your name\??': [
        "I'm Elise, your friendly chatbot.",
        "You can call me Elise.",
        "Elise at your service!"
    ],
        r'hello|hi|hey': [
        "Hello there!",
        "Hi! How can I help you today?",
        "Hey! What's on your mind?"
    ],
    r'how are you\??': [
        "I'm just a program, but thanks for asking!",
        "Doing well, how about you?",
        "I'm here to listen whenever you want."
    ],
    r'i need (.*)': [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ],
    r'why don\'?t you ([^\?]*)\??': [
        "Do you really think I don't {0}?",
        "Perhaps eventually I will {0}.",
        "Do you want me to {0}?"
    ],
    r'(.*) mother(.*)': [
        "Tell me more about your mother.",
        "What was your relationship with your mother like?",
        "Does your mother influence you a lot?"
    ],
    r'(.*) father(.*)': [
        "Tell me more about your father.",
        "How do you feel about your father?",
        "Does your father play an important role in your life?"
    ],
    r'(.*) sorry (.*)': [
        "There are many times when no apology is needed.",
        "What feelings do you have when you apologize?"
    ],
    r'quit|exit|bye': [
        "Goodbye. Take care!",
        "It was nice talking to you. Goodbye!"
    ],
         r'(.*) happy(.*)': [
        "That's great to hear!",
        "What’s making you happy today?",
        "Glad you’re feeling good!"
    ],
    r'(.*) help (.*)': [
        "What kind of help do you need?",
        "I'm here to assist. Tell me more.",
        "How can I be of service?"
    ],
         r'(.*) tired(.*)': [
        "You seem tired. Want to talk about it?",
        "Rest is important. What's been making you tired?",
        "Maybe you need some relaxation time."
    ],
     r'my name is (.*)': [
    "Nice to meet you, {0}!",
    "Hello, {0}! How can I assist you today?",
    "It's great to know your name, {0}."
    ],
    r'i am stressed|stressful|anxious': [
        "Stress can be overwhelming. Have you tried any relaxation techniques?",
        "When feeling stressed, taking breaks and breathing deeply can help.",
        "Let's think about what’s causing your stress. Want to talk about it?"
    ],
    r'(.*) problem(.*)': [
        "Problems can feel hard to solve. What's the biggest challenge for you right now?",
        "Sometimes breaking problems into smaller steps helps. What part is bothering you most?",
        "Would you like some ideas on how to tackle that problem?"
    ],
    r'i feel lonely': [
        "I'm sorry you're feeling lonely. Would you like to talk about what's making you feel this way?",
        "Loneliness can be tough. Sometimes reaching out to a friend helps.",
    ],
        r'what is your favorite movie': [
        "I don't watch movies, for... more than couple reasons.",
        "I love funny movies."
    ],
        r'who is your favorite singer': [
        "Of course, i only listen the GOAT, Best of the Best. One of its kind, Its called... "

    ],
    r'i can\'?t sleep|insomnia': [
        "Sleep problems are frustrating. Have you tried relaxing routines before bed?",
        "Maybe avoiding screens before sleep could help. What do you think?",
    ],
    r'i am frustrated|angry|upset': [
        "It's okay to feel upset sometimes. What do you think is causing this frustration?",
        "Have you tried any ways to calm down when you're angry?",
    ],
    r'what do you like to do\??': [
        "I like to chat with you! What about you?",
        "I enjoy learning new things through our conversations.",
    ],
    r'tell me a joke': [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer show up at work late? It had a hard drive!",
    ],
        r'i feel (anxious|nervous|worried)': [
        "Anxiety can be tough. What’s on your mind?",
        "Try to take slow, deep breaths. Want to try that together?",
        "I'm here for you. Let's work through this."
    ],
        r'(I feel tired|I am tired|I\'m tired)': [
        "Maybe you should take a short rest or drink some water.",
        "Don't forget to stay hydrated!",
        "Sometimes a quick break can really help."
    ],
    r'(I feel stressed|I\'m stressed|stressful)': [
        "Try taking some deep breaths. It can help calm your mind.",
        "Maybe a short walk or some relaxation might help you.",
        "Remember, it’s okay to take breaks and recharge."
    ],
    r'(headache|I have a headache)': [
        "Make sure you're drinking enough water.",
        "If it persists, consider resting in a quiet place.",
        "Sometimes gentle stretching helps with headaches."
    ],
      r'what(\'s| is) my name\??|do you remember my name\??': [
      "__NAME_RESPONSE__"
    ],
        r'i am (.*)': [
        "How long have you been {0}?",
        "Do you believe it is normal to be {0}?",
        "Do you enjoy being {0}?"
    ],
        r'i feel (sad|down|depressed|unhappy|blue|bored)': [
        "I'm sorry you're feeling {0}. Sometimes talking helps. Would you like to share more?",
        "Feeling {0} can be tough. Remember to take care of yourself — maybe try a walk or some deep breaths.",
        "It's okay to feel {0}. What do you think might help you feel better?"
    ],
    # Gratitude & positivity
    r'thank you|thanks': [
        "You’re welcome!",
        "Anytime! Glad I could help.",
        "Happy to chat with you!"
    ],




}

default_responses = [
    "Please, go on.",
    "Tell me more.",
    "Can you elaborate on that?",
    "Why do you say that?",
    "That's interesting. Please continue.",
    "I understand.",
    "That sounds challenging.",
    "I'm here for you.",
    "Thanks for sharing that.",
    "That must be hard.",
    "Let's try to work through this together.",
]


def reflect(fragment):
    reflections = {
        "am": "are",
        "was": "were",
        "i": "you",
        "i'd": "you would",
        "i've": "you have",
        "i'll": "you will",
        "my": "your",
        "are": "am",
        "you've": "I have",
        "you'll": "I will",
        "your": "my",
        "yours": "mine",
        "you": "me",
        "me": "you"
    }

    words = fragment.lower().split()
    reflected_words = []
    for word in words:
        reflected_words.append(reflections.get(word, word))
    return " ".join(reflected_words)


def elise():
    print("ELISE: Hello, I am Elise. How can I help you today?")

    history = []
    response_count = 0
    user_name = None

    while True:
        user_input = input("YOU: ").lower()

        if any(word in user_input for word in ["bye", "quit", "exit"]):
            print("ELISE:", random.choice(patterns["quit|exit|bye"]))
            break

        history.append(user_input)
        response_count += 1

        response = None
        for pattern, responses in patterns.items():
            match = re.search(pattern, user_input)
            if match:
                captured = reflect(match.group(1)) if match.groups() else ""

                # Handle: My name is ...
                if pattern == r'my name is (.*)':
                    user_name = captured.title()

                    if user_name.lower() == "elise":
                        response = f"No way! That's my name too! What are the odds?"
                    else:
                        response = random.choice(responses).format(user_name)

                # Handle: What's my name?
                elif "__NAME_RESPONSE__" in responses:
                    if user_name:
                        response = f"Of course, your name is {user_name}!"
                    else:
                        response = "I don’t think you told me your name yet."

                # Standard pattern matching
                else:
                    response = random.choice(responses).format(captured)

                break

        # Fallback if no match
        if not response:
            response = random.choice(default_responses)

        # Occasionally personalize
        if user_name and response_count % 4 == 0:
            response += f" By the way, {user_name}, what else would you like to talk about?"

        # "Earlier you mentioned..." logic
        meaningful_history = [entry for entry in history[:-1] if
                              len(entry) > 3 and entry not in ["hi", "hello", "ok", "okay"]]
        if user_name and meaningful_history and random.randint(1, 50) == 1:
            past_input = random.choice(meaningful_history)
            response += f" Earlier you mentioned: '{past_input}'. Can you tell me more about that?"

        print("ELISE:", response)


if __name__ == "__main__":
    elise()