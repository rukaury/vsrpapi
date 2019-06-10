from neomodel import StructuredNode, UniqueIdProperty, StringProperty, BooleanProperty, RelationshipTo


class Room(StructuredNode):
    """
    Class to represent the VSR room node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
    active = BooleanProperty()

    # traverse outgoing PARTICIPANT relationship, inflate Users who are in the room
    participant = RelationshipTo("app.models.user.User", 'PARTICIPANT')
    # traverse outgoing CREATED_BY relationship, inflate User who created/owns the room
    admin = RelationshipTo("app.models.user.User", 'CREATED_BY')
    # traverse the PRACTICES relations, inflate the class it studies
    studies = RelationshipTo("app.models.course.Course", 'PRACTICES')

    def json(self):
        """
        Json representation of the room model.
        :return name: the name of the room entered by the admin
        :return active: flag representing if the room is active (true) or disabled (false)
        :return rid: the uuid of the room
        """
        return {"name": self.name,
                "active": self.active,
                "rid": self.uuid
                }
