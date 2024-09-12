from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


@dataclass

class Reminder:

    date_time: datetime
    EMAIL: str = "email"
    SYSTEM: str = "system"
    type: str = EMAIL

    def __str__(self):
        return f"Reminder on {self.date_time} of type {self.type}"

@dataclass

class Event:

    title: str
    description:  str
    date_: date
    start_at: time
    end_at: time

    reminders: list[Reminder] = field(default_factory = list)

    id: str = field(default_factory = generate_unique_id)

    def add_reminder(self, date_time: datetime, type: str = Reminder.EMAIL):
        reminder = Reminder(date_time = date_time, type=type)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if 0 <= reminder_index < len(self.reminders):
            del self.reminders[reminder_index]
        else:
            reminder_not_found_error()

    def __str__(self )-> str:
        ID: {id}
        Event_title: {Event.title}
        Description: {Event.description}
        Time: {Event.start_at} - {Event.end_at}

class Day:

    date_: date
    slots: dict[time, str | None] = []













