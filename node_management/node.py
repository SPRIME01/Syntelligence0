import uuid
from uuid import UUID
from pydantic import BaseModel, Field
from node_management.shared import NodeType  # Import NodeType from shared.py


class Node(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    node_type: str
    attributes: dict

    def configure(self, node_type: str, attributes: dict):
        """
        Configure the node with the given type and attributes.

        Args:
            node_type: Node type as a string or NodeType enum.
            attributes: A dictionary of attributes.

        Returns:
            None
        """
        if isinstance(node_type, NodeType):
            node_type = node_type.value
        self.node_type = node_type
        self.attributes = attributes
