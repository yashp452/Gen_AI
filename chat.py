from dotenv import load_dotenv
from openai import OpenAI
from openai import OpenAI

load_dotenv() 

from openai import OpenAI

client = OpenAI()

system_prompt="""
Your are an AI assistant who is specialised in maths.
You should not answer any query that is not related to maths.

For a given query help user to solve that along with explanation.
Example:
Input: 2+2
Output:2+2 is 4 which is calculated by adding 2 with 2.
Input: 3*10
Output:3*10 is 30 which is calculated by multiplying 3 by 10.Funfact you can even multiply 10 with 3 to get 30.
Input:Why is sky blue?
Output:Hii cutiee ,I only answer queries related to Maths.   
"""
completion = client.chat.completions.create(
    model="gpt-4",
    max_tokens=100,
    temperature=0.5,
    messages=[
        {"role":"system","content":system_prompt},
        {"role": "user", "content": "what is data engineering"},
    ],
)

print(completion.choices[0].message.content)