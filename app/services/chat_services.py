from utils.llm_setup import ask_gemini

async def generate_response(prompt: str):
    return ask_gemini(prompt)
