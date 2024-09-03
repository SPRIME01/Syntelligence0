from dataclasses import dataclass

@dataclass
class Attribute:
    name: str
    type: str

class AttributeRegistry:
    def __init__(self):
        self.attributes = {}

    def add_attribute(self, attribute: Attribute):
        self.attributes[attribute.name] = attribute

    def get_attribute(self, attribute_name: str) -> Attribute:
        return self.attributes.get(attribute_name, None)
