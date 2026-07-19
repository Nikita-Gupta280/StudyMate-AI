import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_file(file):
    files = {
        "file": (file.name, file.getvalue(), file.type)
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

    return response.json()


def ask_ai(question: str):
    response = requests.post(
        f"{BASE_URL}/chat",
        json={"question": question}
    )

    return response.json()


def generate_quiz():
    response = requests.post(f"{BASE_URL}/quiz")
    return response.json()


def generate_flashcards():
    response = requests.post(f"{BASE_URL}/flashcards")
    return response.json()