from pydantic import BaseModel, Field
from uuid import UUID
from node_management.shared import NodeType  # Import NodeType from shared.py

class Node(BaseModel):
    id: UUID = Field(default_factory=UUID)
    name: str
    node_type: str
    attributes: dict

    def configure(self, node_type: str, attributes: dict):
        if isinstance(node_type, NodeType):
            node_type = node_type.value
        self.node_type = node_type
        self.attributes = attributes
