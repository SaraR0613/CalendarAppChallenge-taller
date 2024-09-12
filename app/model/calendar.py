from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

import app.services.util
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

    reminders: list[Reminder] = field(init = False, default_factory = list)

    id: str = app.services.util.generate_unique_id()

    def add_reminder(self, date_time: datetime, type: str = Reminder.EMAIL):
        reminder = Reminder(date_time=date_time, type=type)
        self.reminders.append(reminder)

    def delete_reminder(self, reminder_index: int):
        if self.reminders[reminder_index] in self.reminders:
            return self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def __str__(self):
        f"ID: {self.id} - Event_title: {self.title}\n Description: {Event.description}\n Time: {Event.start_at}\n {Event.end_at})"


class Day:
    date_: date
    slots: dict[time, str | None] = {}

    def _init_slots(self):
        pass

    def add_event(self, event_id: str, start_at: time, end_at: time):
        pass


    def delete_event(self, event_id: str):
        deleted = False
        for slot, saved_id in self.slots.items():
            if saved_id == event_id:
                self.slots[slot] = None
                deleted = True
        if not deleted:
            event_not_found_error()

    def update_event(self, event_id: str, start_at: time, end_at: time):
        for slot in self.slots:
            if self.slots[slot] == event_id:
                self.slots[slot] = None

        for slot in self.slots:
            if start_at <= slot < end_at:
                if self.slots[slot]:
                    slot_not_available_error()
                else:
                    self.slots[slot] = event_id

















