Feature: Node Configuration Management

  Scenario: Configure a New Node

  Given the ARP + AutoARP system is initialized
  And the system has existing node types: "Human", "AI Agent", "Internal API Endpoint", "External API Endpoint", "Group"
  When an administrator configures a new node of type "AI Agent" with attributes
  And the node is assigned the ID "node_1"
  Then the new node should be added to the system
  And it should have the specified type and ID
