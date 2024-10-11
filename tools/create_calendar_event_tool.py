from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type
from functions.calendar_function import create_event


class CalendarCreateInput(BaseModel):
    """Inputs for create_calendar_event"""

    calendar_id: str = Field(description="calendar id of the calendar")
    event_name: str = Field(description="name of the event")
    start_datetime: str = Field(
        description="Start datetime of the event to create. Must be an RFC3339 timestamp, no need for timezone for example, 2011-06-03T10:00:00-07:00, 2011-06-03 "
    )
    end_datetime: str = Field(
        description="End datetime of the event to create. Must be an RFC3339 timestamp, no need for timezone for example, 2011-06-03T10:00:00-07:00, 2011-06-03"
    )


class CreateCalendarEventTool(BaseTool):
    name = "create_calendar_event"
    description = """
Useful when you want to create a calendar event given a calendar id, event name, start time, and end time.
"""
    args_schema: Type[BaseModel] = CalendarCreateInput

    def _run(
            self,
            calendar_id: str,
            event_name: str,
            start_datetime: str,
            end_datetime: str,
    ):
        events_response = create_event(
            calendar_id, event_name, start_datetime, end_datetime
        )
        return events_response

    def _arun(self):
        raise NotImplementedError("create_calendar_event does not support async")
