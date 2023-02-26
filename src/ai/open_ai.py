import os
from dotenv import load_dotenv
import openai


def configure():
    load_dotenv()
    openai.api_key = os.getenv('TOKEN')

def get_application_category(text) -> str:
    
    categories = ['gaming', 'working', 'entertainment', 'learning']
    c = ", ".join(categories)
    #print(c)
    # Utilizza OpenAI per classificare la categoria del testo
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=(
            f"Classify the following app into one of the following categories: university, learning, working, gaming, or entertainment:\n\n{text}\n\nCategory: "
            #f"Classify the following app into one of the following categories: {c}:\n\n{text}\n\nCategory: "
        ),
        temperature=0.5,
        max_tokens=1,
        n=1,
        stop=None,
        timeout=10,
    )

    # Restituisce la categoria predetta
    category = response.choices[0].text.strip().lower()
    return category


if __name__ == '__main__':
    configure()
    print(get_application_category("waste tracker"))


def main():
    configure()