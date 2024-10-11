from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from datetime import datetime


class SpecificTimeInput(BaseModel):
    """Inputs for setting a specific time"""

    year: int = Field(description="Year of the event")
    month: int = Field(description="Month of the event")
    day: int = Field(description="Day of the event")
    hour: int = Field(description="Hour of the event")
    minute: int = Field(description="Minute of the event")


class SpecificTimeTool(BaseTool):
    name = "set_specific_time"
    description = "Sets a specific time for an event, for example when you want to create an event at 3pm on June 3rd, 2021."
    args_schema: Type[BaseModel] = SpecificTimeInput

    def _run(self, year: int, month: int, day: int, hour: int, minute: int):
        specific_time = datetime(year, month, day, hour, minute)
        return specific_time.strftime("%Y-%m-%dT%H:%M:%S%z")

    def _arun(self):
        raise NotImplementedError("set_specific_time does not support async")
