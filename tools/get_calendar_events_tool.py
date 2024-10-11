from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from functions.calendar_function import get_calendar_events
from typing import Type


class CalendarEventSearchInput(BaseModel):
    """Inputs for get_calendar_events"""

    calendar_id: str = Field(description="Calendar id of the calendar")
    start_date: str = Field(
        description="Start date of the events to search. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. "
    )
    end_date: str = Field(
        description="End date of the events to search. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z."
    )
    include_event_ids: bool = Field(
        description="Whether to return the event ids or not. You only need them if you are going to use them for another function."
    )


class GetCalendarEventsTool(BaseTool):
    name = "get_calendar_events"
    description = """
        Useful when you want to get calendar events in a particular date or time range after you have retrieved the current time.
        """
    args_schema: Type[BaseModel] = CalendarEventSearchInput

    def _run(self, calendar_id: str, start_date: str, end_date: str, include_event_ids: bool):
        events_response = get_calendar_events(calendar_id, start_date, end_date, include_event_ids)
        return events_response

    def _arun(self):
        raise NotImplementedError("get_calendar_events does not support async")
