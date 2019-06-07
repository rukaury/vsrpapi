from neomodel import StructuredNode, StringProperty, BooleanProperty, RelationshipTo


class Answer(StructuredNode):
    """
    Class to represent the Answer node
    """
    text = StringProperty()
    correct = BooleanProperty()
    # traverse the ANSWERED_FOR relationship, inflate the question the answer belongs to
    answer_for = RelationshipTo(Question, 'ANSWER_FOR')
