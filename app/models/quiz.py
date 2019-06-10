from neomodel import (StructuredNode, StringProperty,
                      UniqueIdProperty, RelationshipTo, One, RelationshipFrom, OneOrMore)
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
                                 "ASKED_BY", cardinality=One, model=BaseRel)
