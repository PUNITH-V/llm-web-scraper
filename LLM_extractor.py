from groq import Groq
import os
from dotenv import load_dotenv
from prompt_template import system_prompt, user_prompt
from scraper import scrape, clean

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def call_llm(system_prompt :str, user_prompt :str) -> str:
    response = client.chat.completions.create(
         model="openai/gpt-oss-120b",
         
         messages=[
             {
                 
                 "role": "system",
                 "content": system_prompt
             },
             {
                 "role": "user",
                 "content": user_prompt
             }
         ],
            max_tokens=2000,
            temperature=0.2,
            include_reasoning=False
    )

    return response.choices[0].message.content
      