from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type, Optional
from datetime import datetime, timedelta


class TimeDeltaInput(BaseModel):
    """Inputs for getting time deltas"""

    delta_days: Optional[int] = Field(
        description="Number of days to add to the current time. Must be an integer."
    )
    delta_hours: Optional[int] = Field(
        description="Number of hours to add to the current time. Must be an integer."
    )
    delta_minutes: Optional[int] = Field(
        description="Number of minutes to add to the current time. Must be an integer."
    )
    delta_seconds: Optional[int] = Field(
        description="Number of seconds to add to the current time. Must be an integer."
    )



class TimeDeltaTool(BaseTool):
    name = "get_future_time"
    description = """
Useful when you want to get a future time in an RFC3339 timestamp, given a time delta such as 1 day, 2 hours, 3 minutes, 4 seconds. 
"""
    args_schema: Type[BaseModel] = TimeDeltaInput

    def _run(
            self,
            delta_days: int = 0,
            delta_hours: int = 0,
            delta_minutes: int = 0,
            delta_seconds: int = 0,
    ):
        # Return the current time in a format google calendar api can understand
        return (
                datetime.utcnow()
                + timedelta(
            days=delta_days,
            hours=delta_hours,
            minutes=delta_minutes,
            seconds=delta_seconds
        )
        ).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def _arun(self):
        raise NotImplementedError("get_future_time does not support async")
