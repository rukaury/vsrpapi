from neomodel import (StructuredNode, StringProperty,
                      UniqueIdProperty, RelationshipTo, One, RelationshipFrom, ZeroOrMore)
from app.models.relationships.base_rel import BaseRel


class Quiz(StructuredNode):
    """
    Class to represent the Quiz node
    """

    uuid = UniqueIdProperty()
    name = StringProperty(required=True)
    # traverse the ASKED_IN relations, inflate the room the question is a part of
    room = RelationshipTo("app.models.room.Room",
                          "ASKED_IN", cardinality=One, model=BaseRel)
    # traverse the ASKED_By relationship, inflate the question the quiz conatins
    questions = RelationshipFrom("app.models.question.Question",
                                 "ASKED_BY", cardinality=ZeroOrMore, model=BaseRel)

    def update(self, name, rel):
        """
        Function will update the course
        :param code: the new course code
        """

        self.name = name if name is not None else self.name
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
            "room": self.room.get().json(),
            "uuid": self.uuid
        }
