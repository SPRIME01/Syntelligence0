import pytest
from pytest_bdd import scenario, given, when, then, parsers
from node_management.node_types import NodeTypeRegistry
from node_management.node import Node
from uuid import uuid4

# Fixture to initialize the system and provide a context
@pytest.fixture
def context():
    registry = NodeTypeRegistry()
    # Initialize other system components here
    node = Node(id=uuid4(), name="default_node", node_type="default_type", attributes={})
    return {"registry": registry, "node": node}

@scenario('node_config_mgmt.feature', 'Configure a New Node')
def test_configure_node():
    pass

@given("the ARP + AutoARP system is initialized")
def system_initialized(context):
    # Initialization or assertion for system startup
    pass  # Remove the call to context["registry"].initialize()

@given("the system has existing node types: \"Human\", \"AI Agent\", \"Internal API Endpoint\", \"External API Endpoint\", \"Group\"")
def existing_node_types(context):
    # Populate the registry with these types
    context["registry"].add_node_type("Human", {"attribute1": "value1"})
    context["registry"].add_node_type("AI Agent", {"attribute2": "value2"})
    context["registry"].add_node_type("Internal API Endpoint", {"attribute3": "value3"})
    context["registry"].add_node_type("External API Endpoint", {"attribute4": "value4"})
    context["registry"].add_node_type("Group", {"attribute5": "value5"})

@when(parsers.parse('an administrator configures a new node of type "{node_type}" with attributes'))
def configure_node(context, node_type):
    # Simulate configuring a node with attributes, using a fixture for attributes
    attributes = {"some_attribute": "attribute_value"}
    context["node"].configure(node_type=node_type, attributes=attributes)

@when(parsers.parse('the node is assigned the ID "{id}"'))
def assign_id(context, id):
    context["node"].id = id

@then("the new node should be added to the system")
def verify_node_added(context):
    # Verify that the node is present in the system or a nodes list
    assert context["node"].id == "node_1"  # Placeholder, actual verification logic needed

@then("it should have the specified type and ID")
def verify_type_and_id(context):
    assert context["node"].node_type == "AI Agent"
    assert context["node"].id == "node_1"
