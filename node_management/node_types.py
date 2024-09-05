from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class NodeTypeRegistry:
    """Registry of node types."""

    def __init__(self):
        """
        Initialize the node type registry.

        The registry is a dictionary mapping node type names to dictionaries
        containing the attributes of the node type. The keys of the inner
        dictionaries are the attribute names, and the values are lists of strings
        representing the attribute values.
        """
        self.node_types: Dict[str, Dict[str, List[str]]] = field(default_factory=dict)

    def initialize(self) -> None:
        """Initialize the registry with default node types"""
        self.add_node_type("HUMAN", ["attribute1"])
        self.add_node_type("AI_AGENT", ["attribute1"])
        self.add_node_type("INTERNAL_API_ENDPOINT", ["attribute1"])
        self.add_node_type("EXTERNAL_API_ENDPOINT", ["attribute1"])
        self.add_node_type("GROUP", ["attribute1"])

    def add_node_type(self, node_type: str, attributes: List[str]) -> None:
        """Add a node type to the registry.

        Args:
            node_type: The name of the node type.
            attributes: A list of attributes for the node type.
        """
        if node_type not in self.node_types:
            self.node_types[node_type] = {"attributes": attributes}

    def get_node_type(self, node_type: str) -> Dict[str, List[str]]:
        """Get a node type from the registry.

        Args:
            node_type: The name of the node type.

        Returns:
            A dictionary with the node type and its attributes.
        """
        return self.node_types.get(node_type, {"attributes": []})

    def get_all_node_types(self) -> List[str]:
        """Get all node types from the registry.

        Returns:
            A list of node types.
        """
        return list(self.node_types.keys())
