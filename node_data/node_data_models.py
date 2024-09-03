# Defines node data models
# Required imports: dataclasses, typing
import pydantic.dataclasses as py_dataclass
import UUID 


@py_dataclass.dataclass
class Node: 
    id: UUID
    name: str
    node_type: str
    attributes: dict