import openai
import time
import sys

openai.api_key = "API_KEY"

def ask_question(history):
    """Send history to OpenAI and get the next question."""
    prompt = f"""
You are playing a 20-questions style guessing game.
Rules:
1. The user will only answer with: 1 = Yes, 2 = No, 3 = I don't know.
2. Ask logical yes/no questions to guess who the person/character is.
3. Do NOT make a guess unless explicitly told.
History so far:
{history}

Your next question:
"""
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def make_guess(history):
    """Force the model to make its best guess."""
    prompt = f"""
Based on the following history, make your best guess now.
History:
{history}

Respond only in this format: "I guess you are (character)".
"""
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_valid_input(prompt, valid_options):
    """Keep asking until user gives valid input."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def print_thinking(message="Thinking", duration=2, interval=0.5):
    """Simulate thinking with a loading dots effect."""
    print(message, end="")
    sys.stdout.flush()
    elapsed = 0
    while elapsed < duration:
        print(".", end="")
        sys.stdout.flush()
        time.sleep(interval)
        elapsed += interval
    print()

def main():
    print("Think of a famous person, character, or figure.")
    print("Answer questions with: 1 = Yes, 2 = No, 3 = I don't know.\n")

    history = ""

    for i in range(1, 51):
        print_thinking("Thinking of the next question")
        question = ask_question(history)
        print(f"Q{i}: {question}")
        answer = get_valid_input("Your answer (1 = Yes, 2 = No, 3 = I don't know): ", ["1", "2", "3"])
        history += f"\nQ{i}: {question}\nA{i}: {answer}"

        if i == 20 or (i > 20 and i % 5 == 0):
            print_thinking("Making my guess")
            guess = make_guess(history)
            print("\n" + guess)
            confirm = get_valid_input("Is this correct? (1 = Yes, 2 = No): ", ["1", "2"])
            if confirm == "1":
                print("Yay! I guessed it right 🎉")
                break
            else:
                print("Okay, I'll keep going...\n")

if __name__ == "__main__":
    main()
