from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=api_key)

while True:
    if user_inpupt == "exit":
        break
    else
        user_inpupt = input("enter your expression :")
        response = model.invoke(user_inpupt)
        print(response.content)
