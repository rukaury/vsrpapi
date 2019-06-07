from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo


class Quiz(StructuredNode):
    """
    Class to represent the Quiz node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
    # traverse the ASKED_IN relations, inflate the room the question is a part of
    asked_in = RelationshipTo(Room, 'ASKED_IN')
