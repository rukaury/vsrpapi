from neomodel import StructuredNode, StringProperty, BooleanProperty, RelationshipTo, OneOrMore, UniqueIdProperty
from app.models.relationships.base_rel import BaseRel


class Question(StructuredNode):
    """
    Class to represent the Question node
    """
    uuid = UniqueIdProperty()
    title = StringProperty(required=True)
    text = StringProperty()
    is_multiple_choice = BooleanProperty()
    # traverse the ASKED_BY relationship, inflate the quiz this question belongs to
    quiz = RelationshipTo("app.models.quiz.Quiz",
                          "ASKED_BY", cardinality=One, model=BaseRel)
    # traverse the ANSWERED_FOR relationship, inflate the answers to the question
    answers = RelationshipFrom(
        "app.models.question.Question", "ANSWER_FOR", cardinality=OneOrMore, model=BaseRel)

    def update(self, title, text, rel):
        """
        Function will update the course
        :param code: the new course code
        """

        self.title = title if title is not None else self.title
        self.text = text if text is not None else self.text
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
            "title" : self.title,
            "text" : self.text,
            "uuid" : self.uuid,
            "quiz" : self.quiz.get().json()
        }
