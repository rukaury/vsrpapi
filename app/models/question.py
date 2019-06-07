from neomodel import StructuredNode, StringProperty, BooleanProperty, RelationshipTo


class Question(StructuredNode):
    """
    Class to represent the Question node
    """
    title = StringProperty()
    text = StringProperty()
    is_multiple_choice = BooleanProperty()
    # traverse the ASKED_BY relationship, inflate the quiz the question belongs to
    asked_by = RelationshipTo(Quiz, 'ASKED_BY')
