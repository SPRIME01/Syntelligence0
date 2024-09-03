from dataclasses import dataclass
from node_management.shared import NodeType  # Import NodeType from node_management.shared

@dataclass
class NodeTypeRegistry:
    def __init__(self):
        self.node_types = {
            nt.value: {"attributes": nt.attributes}  # Use the attributes defined in NodeType
            for nt in NodeType
        }

    def initialize(self):
        # Add any initialization logic here
        pass

    def add_node_type(self, node_type: str, attributes: list):
        if node_type not in self.node_types:
            self.node_types[node_type] = {"attributes": attributes}

    def get_node_type(self, node_type: str) -> dict:
        return self.node_types.get(node_type, {})

    def get_all_node_types(self) -> list:
        return list(self.node_types.keys())
