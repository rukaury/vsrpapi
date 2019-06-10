from neomodel import StructuredNode, StringProperty, UniqueIdProperty, RelationshipTo, ZeroOrMore
from app.models.relationships.base_rel import BaseRel


class Quiz(StructuredNode):
    """
    Class to represent the Quiz node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
    # traverse the ASKED_IN relations, inflate the room the question is a part of
    asked_in = RelationshipTo("app.models.room.Room",
                              'ASKED_IN', cardinality=ZeroOrMore, model=BaseRel)
