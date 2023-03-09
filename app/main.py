from fastapi import FastAPI, status, HTTPException, Body
from rich import print
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"

chatgpt_context = """
As a Senior Network/Firewall Engineer, you are tasked with troubleshooting a network issue that is causing high CPU utilization. 
You are given the output of debug commands and asked to review them to determine the potential cause of the issue. 
Your task is to identify the underlying problem and provide recommendations on how to resolve it, do not provide any configuration commands. Pay
close attention to the processes from the diagnose sys top command.
This is a fortigate firewall.
"""


@app.post("/fortigate/troubleshoot/")
async def troubleshoot_fortigate(body: str = Body(...)):
    print(body)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"{chatgpt_context}."},
                {"role": "user", "content": f"{body}"},
            ],
        )
        message = response.choices[0]["message"]
        print(f"[bold yellow]:robot_face: ChatGPT Response[/bold yellow] :robot_face:")
        print(message["content"])
        print(f"[bold yellow]:robot_face: ChatGPT Response[/bold yellow] :robot_face:")
        return status.HTTP_200_OK
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
