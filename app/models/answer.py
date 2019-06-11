from neomodel import (StructuredNode, StringProperty,
                      BooleanProperty, RelationshipTo, One, UniqueIdProperty)
from app.models.relationships.base_rel import BaseRel


class Answer(StructuredNode):
    """
    Class to represent the Answer node
    """
    uuid = UniqueIdProperty()
    text = StringProperty(required=True)
    correct = BooleanProperty(required=True)
    # traverse the ANSWERED_FOR relationship, inflate the question the answer belongs to
    question = RelationshipTo(
        "app.models.question.Question", "ANSWER_FOR", cardinality=One, model=BaseRel)

    def update(self, text, rel):
        """
        Function will update the course
        :param code: the new course code
        """

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
            "text": self.text,
            "correct": self.correct,
            "uuid": self.uuid
        }
