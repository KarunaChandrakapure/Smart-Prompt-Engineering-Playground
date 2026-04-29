import time
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_prompt(prompt,model="gpt-5-mini"):
    start=time.time()
    response = client.responses.create(
        model = model,
        input = prompt
    )
    latency = round(time.time()-start,2)

    return {
        "output": response.output_text,
        "latency": latency,
        "tokens" : getattr(response,"usage",None),
    }

output = run_prompt('I liked the pizza')
print(output)