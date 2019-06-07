from neomodel import StructuredNode, UniqueIdProperty, StringProperty, BooleanProperty, RelationshipTo


class Room(StructuredNode):
    """
    Class to represent the VSR room node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
    active = BooleanProperty()

    # traverse outgoing PARTICIPANT relationship, inflate Users who are in the room
    participant = RelationshipTo(User, 'PARTICIPANT')
    # traverse outgoing CREATED_BY relationship, inflate User who created/owns the room
    admin = RelationshipTo(User, 'CREATED_BY')
    # traverse the PRACTICES relations, inflate the class it studies
    studies = RelationshipTo(Course, 'PRACTICES')
