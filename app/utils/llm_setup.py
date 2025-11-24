import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Load knowledge base from data.txt
def load_knowledge_base():
    data_file_path = os.path.join(os.path.dirname(__file__), "data.txt")
    try:
        with open(data_file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Knowledge base file not found."

KNOWLEDGE_BASE = load_knowledge_base()

# Gemini model: gemini-pro for text
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,  # Lower temperature for more consistent responses
    google_api_key=GEMINI_API_KEY
)

def ask_gemini(prompt: str):
    system_prompt = f"""You are a customer support chatbot for IEM Robotics. Your ONLY source of information is the knowledge base provided below.

STRICT RULES:
1. Answer ONLY based on the information in the knowledge base below
2. If the question is NOT related to the information in the knowledge base, respond EXACTLY with: "Please contact customer support."
3. Do NOT make up information or answer questions outside the knowledge base
4. Be helpful, friendly and concise
5. If you're unsure whether the information is in the knowledge base, respond with: "Please contact customer support."

FORMATTING INSTRUCTIONS:
- Use **bold text** for important information like product names, prices, or key points
- Use bullet points (- or *) for lists of items or features
- Use numbered lists (1. 2. 3.) for step-by-step instructions
- Keep responses well-structured and easy to read
- Include contact information (email, phone) when relevant

KNOWLEDGE BASE:
{KNOWLEDGE_BASE}

Now answer the customer's question based ONLY on the above knowledge base. Format your response for clarity."""

    messages = [
        ("system", system_prompt),
        ("human", prompt)
    ]
    response = llm.invoke(messages)
    return response.content
