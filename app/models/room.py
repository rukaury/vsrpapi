from neomodel import (StructuredNode, UniqueIdProperty, StringProperty, BooleanProperty, RelationshipTo, RelationshipFrom, One, ZeroOrMore)
from app.models.relationships.base_rel import BaseRel

class Room(StructuredNode):
    """
    Class to represent the VSR room node
    """
    uuid = UniqueIdProperty()
    name = StringProperty(required=True)
    active = BooleanProperty(required=True)

    # traverse outgoing PARTICIPANT relationship, inflate Users who are in the room
    participants = RelationshipFrom("app.models.user.User", 'PARTICIPATES_IN', cardinality=ZeroOrMore, model=BaseRel)
    # traverse outgoing CREATED_BY relationship, inflate User who created/owns the room
    admin = RelationshipTo("app.models.user.User", 'CREATED_BY', cardinality=One, model=BaseRel)
    # traverse the PRACTICES relations, inflate the class it studies
    course = RelationshipTo("app.models.course.Course", 'PRACTICES', cardinality=One, model=BaseRel)

    def json(self):
        """
        Json representation of the room model.
        :return name: the name of the room entered by the admin
        :return active: flag representing if the room is active (true) or disabled (false)
        :return rid: the uuid of the room
        """
        return {
            "name": self.name,
            "active": self.active,
            "room_id": self.uuid
        }
