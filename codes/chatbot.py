from google import genai#Python communicate with Gemini models.This imports the Google Gemini SDK.
from dotenv import load_dotenv# Load .env file
import os

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

print("Simple Gemini Chatbot")
print("Type 'exit' to quit.\n")

# Main loop (take input and generate response)
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )
    print("Bot:", response.text)