# Defines node data models
# Required imports: dataclasses, typing
from dataclasses import dataclass
from typing import Dict
import uuid


@dataclass
class Node:
    id: uuid.UUID
    name: str
    node_type: str
    attributes: Dict[str, str]
