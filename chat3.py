from dotenv import load_dotenv
import os
import json
from openai import OpenAI
import requests
load_dotenv()

client=OpenAI()

def get_weather(city:str):
    print(f"tool called for {city}")
    url=f"https://wttr.in/{city}?format=%C+%t"
    response=requests.get(url)
    if response.status_code==200:
        return f"The weather in {city} is {response.text}"
    return "100 degree Celsius"



available_tools={
    "get_weather":{
        "fn":get_weather,
        "description":"Takes a city name as input and returns the current weather for the city"
    },
    "run_command":{
        "fn":run_command,
        "description":"Takes a command as input to execute on syatem and returns output"
    }
}
system_prompt="""
You are an helpful AI assiatant who is specialised in resolving user query.
You work on start,plan,action,observe mode.
For the given user query and available tools,plan the step by step execution,  based on planning.
select the relevant tool from available tool.and based on thr tool selection you perform an action
to call the tool.
Wait for the observation and based on observation from the tool call resolve the user query.

Rules:
-Follow the output JSON format
-Always perform one step ata timer and wait for next input

Output JSON format:
{{
"step":"string",
"content":"string",
"function":"The name  of function if the step is action",
"input":"The input parameter for function"
}}

Available Tools:
-get weather : Takes a city name as input and returns the current weather for the city
-run_command:Takes a command as input to execute on syatem and returns output

Example:
User Query:What is the weather of new York?
Output:{{"step":"plan","content":"The user is interested in weather data of new york"}}
Output:{{"step:"plan","content":"From the available tools I should call get_weather"}}
Output:{{"step":"action","function":"get_weather","input":"new york"}}
Output:{{"step":"observe","output":"12 Degree Cel"}}
Output:{{"step":"output","content":"The weather of new york seems to be 12 degrees"}}
"""
messages=[
    {"role":"system","content":system_prompt}
]
user_query=input("> ")
messages.append({"role":"user","content":user_query})

while True:
    response=client.chat.completions.create(
        model="gpt-4o",
        response_format={"type":"json_object"},
        messages=messages
    )
    parsed_output=json.loads(response.choices[0].message.content)
    messages.append({"role":"assistant","content":json.dumps(parsed_output)})
    if parsed_output.get("step")=="plan":
        print(f"{parsed_output.get('content')}")
        continue
    if parsed_output.get("step")=="action":
        tool_name=parsed_output.get("function")
        tool_input=parsed_output.get("input")
        if available_tools.get(tool_name,False)!=False:
            output=available_tools[tool_name].get("fn")(tool_input)
            messages.append({"role":"assistant","content":json.dumps({"step":"observe","output":output})})
            continue
    if parsed_output.get("step")=="output":
        print(f"{parsed_output.get('content')}")
        break

