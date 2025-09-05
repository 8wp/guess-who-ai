import openai

openai.api_key = "API"

def ask_question(question, history):
    """Send a question + history to OpenAI and get the next question/guess."""
    prompt = f"""
You are playing a 20-questions style guessing game.
Rules:
1. The user will only answer with: 1 = Yes, 2 = No, 3 = I don't know
2. Ask logical yes/no questions to guess who the person/character is.
3. Every 10 questions, make a guess in the format: "I guess you are (character)".
4. Use history to avoid repeating yourself.
History so far:
{history}

Your next question or guess:
"""

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

def main():
    print("Think of a famous person, character, or figure.")
    print("Answer questions with: 1 = Yes, 2 = No, 3 = I don't know.\n")

    history = ""
    for i in range(1, 21):
        question = ask_question("Next question", history)
        print(question)

        answer = input("Your answer (1/2/3): ").strip()
        history += f"\nQ{i}: {question}\nA{i}: {answer}"

        if "I guess you are" in question:
            confirm = input("Is this correct? (1=Yes, 2=No): ").strip()
            if confirm == "1":
                print("Yay! I guessed it right 🎉")
                break
            else:
                print("Okay, I'll keep going...\n")

if __name__ == "__main__":
    main()
