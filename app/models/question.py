from neomodel import StructuredNode, StringProperty, BooleanProperty, RelationshipTo, OneOrMore
from app.models.relationships.base_rel import BaseRel


class Question(StructuredNode):
    """
    Class to represent the Question node
    """

    title = StringProperty(required=True)
    text = StringProperty()
    is_multiple_choice = BooleanProperty()
    # traverse the ASKED_BY relationship, inflate the quiz this question belongs to
    quiz = RelationshipTo("app.models.quiz.Quiz",
                          "ASKED_BY", cardinality=One, model=BaseRel)
    # traverse the ANSWERED_FOR relationship, inflate the answers to the question
    answers = RelationshipFrom(
        "app.models.question.Question", "ANSWER_FOR", cardinality=One, model=BaseRel)
