import os
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class PushNotificationInput(BaseModel):
    """A message to be send to the user."""
    message: str = Field(..., description="The message to be sent to the user.")

class PushNotificationTool(BaseTool):
    name: str = "Send a push notification"
    description: str = (
        "This tool sends a push notification to the user. "
    )
    args_schema: Type[BaseModel] = PushNotificationInput

    def _run(self, message: str) -> str:
        pushover_user= os.getenv("PUSHOVER_USER")
        pushover_token = os.getenv("PUSHOVER_TOKEN")
        pushover_url= "https://api.pushover.net/1/messages.json"

        print(f"Sending push notification to {pushover_user} with message: {message}")
        payload = {"token": pushover_token,"user": pushover_user,"message": message}
        requests.post(pushover_url, data=payload)
        return "Push notification sent successfully."
    

