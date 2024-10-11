from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from functions.calendar_function import delete_event


class CalendarDeleteInput(BaseModel):
    """Inputs for delete_calendar_event"""

    calendar_id: str = Field(description="calendar id of the calendar")
    event_id: str = Field(
        description="id of the event retrieved from the user's calendar by searching it. must be the FULL event id."
    )


class DeleteCalendarEventTool(BaseTool):
    name = "delete_calendar_event"
    description = """
Useful for when you want to delete an event given a calendar id and an event id. Make sure to pass the FULL event id.
"""
    args_schema: Type[BaseModel] = CalendarDeleteInput

    def _run(self, calendar_id: str, event_id: str):
        events_response = delete_event(calendar_id, event_id)
        return events_response

    def _arun(self):
        raise NotImplementedError("delete_calendar_event does not support async")