from neomodel import (StructuredNode, UniqueIdProperty, StringProperty,
                      BooleanProperty, RelationshipTo, RelationshipFrom, One, ZeroOrMore)
from app.models.relationships.base_rel import BaseRel
import datetime


class Room(StructuredNode):
    """
    Class to represent the VSR room node
    """
    uuid = UniqueIdProperty()
    name = StringProperty(required=True)
    active = BooleanProperty(required=True)

    # traverse outgoing PARTICIPANT relationship, inflate Users who are in the room
    participants = RelationshipFrom(
        "app.models.user.User", 'PARTICIPATES_IN', cardinality=ZeroOrMore, model=BaseRel)
    # traverse outgoing CREATED_BY relationship, inflate User who created/owns the room
    admin = RelationshipTo("app.models.user.User",
                           'CREATED_BY', cardinality=One, model=BaseRel)
    # traverse the PRACTICES relations, inflate the class it studies
    course = RelationshipTo("app.models.course.Course",
                            'PRACTICES', cardinality=One, model=BaseRel)
    # traverse the incoming ASKED_IN relationship, inflate the question class
    questions = RelationshipFrom(
        "app.models.question.Question", "ASKED_IN", cardinality=ZeroOrMore, model=BaseRel)

    def update(self, name, course, rel):
        """
        Function will update the course
        :param code: the new course code
        """

        self.name = name if name is not None else self.name

        if course:
            self.course.reconnect(self.course.get(), course)
        rel.updated_on = datetime.datetime.now()
        self.save()

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
