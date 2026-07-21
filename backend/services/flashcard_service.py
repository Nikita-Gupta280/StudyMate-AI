from services.rag_pipeline import generate_flashcards

def get_flashcards():
    print("🔥 FLASHCARD SERVICE CALLED")
    return generate_flashcards()