from pydantic import BaseModel
from langchain.tools import BaseTool
from typing import Type
from datetime import datetime


class CurrentTimeInput(BaseModel):
    """Inputs for getting the current time"""

    pass


class CurrentTimeTool(BaseTool):
    name = "get_current_time"
    description = """
    Useful when you want to get the current time in an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z.
    """
    args_schema: Type[BaseModel] = CurrentTimeInput

    def _run(self):
        # Return the current time in a format google calendar api can understand
        return (datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),)

    def _arun(self):
        raise NotImplementedError("convert_time does not support async")
