from neomodel import (StructuredNode, StringProperty,
                      BooleanProperty, RelationshipTo, One)
from app.models.relationships.base_rel import BaseRel


class Answer(StructuredNode):
    """
    Class to represent the Answer node
    """

    text = StringProperty(required=True)
    correct = BooleanProperty()
    # traverse the ANSWERED_FOR relationship, inflate the question the answer belongs to
    answer_for = RelationshipTo(
        "app.models.question.Question", "ANSWER_FOR", cardinality=One, model=BaseRel)
