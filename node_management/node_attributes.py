from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Attribute:
    name: str
    type: str


class AttributeRegistry:
    def __init__(self) -> None:
        self.attributes: Dict[str, Attribute] = {}

    def add_attribute(self, attribute: Attribute) -> None:
        self.attributes[attribute.name] = attribute

    def get_attribute(self, attribute_name: str) -> Optional[Attribute]:
        """
        Get an attribute by name.

        Args:
            attribute_name (str): The name of the attribute to retrieve.

        Returns:
            Attribute: The attribute if found, otherwise None.
        """
        return self.attributes.get(attribute_name)
