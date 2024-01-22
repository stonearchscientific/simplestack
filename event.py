from enum import Enum
import java
class Event:
    def __init__(self, name, start, end):
        self.name = name
        self.interval = java.interval(start, end)
class Reference(Event):
    def __init__(self, name, start, end, type=None):
        super().__init__(name, start, end)
        if type is None:
            self.type = Reference.Type.DAY
        else:
            self.type = type

    class Type(Enum):
        YEAR = 1
        QUARTER = 2
        MONTH = 3
        WEEK = 4
        DAY = 5
class Task(Event):
    def __init__(self, name, start, end, id):
        super().__init__(name, start, end, id)
        self.id = id
