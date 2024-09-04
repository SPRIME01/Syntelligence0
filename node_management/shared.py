from enum import Enum
from dataclasses import dataclass


@dataclass
class NodeType(Enum):
    API_ENDPOINT = ("API_ENDPOINT", {"attribute1": "value1"})
    HUMAN = ("HUMAN", {"attribute2": "value2"})
    AI_AGENT = ("AI_AGENT", {"attribute3": "value3"})
    GROUP = ("GROUP", {"attribute4": "value4"})

    def __init__(self, value, attributes):
        self._value_ = value
        self.attributes = attributes
