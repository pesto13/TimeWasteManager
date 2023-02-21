import os
from dotenv import load_dotenv

import openai


def configure():
    load_dotenv()
    openai.api_key = os.getenv('TOKEN')

def get_application_category(text):
    
    categories = ['gaming', 'working', 'entertainment', 'learning']
    c = ", ".join(categories)
    # Utilizza OpenAI per classificare la categoria del testo
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=(
            f"Classify the following app into one of the following categories: learning, coding, or entertainment:\n\n{text}\n\nCategory: "
        ),
        temperature=0,
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
    print(get_application_category("matematica"))



