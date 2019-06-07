from neomodel import (StructuredNode, StringProperty,
                      UniqueIdProperty, RelationshipFrom, ZeroOrMore)
from app.models.relationships.base_rel import BaseRel


class School(StructuredNode):
    """
    Class to represent the School node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
    courses = RelationshipFrom(
        'app.models.course.Course', 'TAUGHT_AT', cardinality=ZeroOrMore, model=BaseRel)

    def update(self, name, rel):
        """
        Function will update the name of the school
        :param name: the name of the school
        """

        self.name = name if name is not None else self.name
        rel.updated_on = datetime.datetime.now()
        self.save()

    def json(self):
        """
        Json representation of the event model.
        :return:
        """
        return {
            'uuid': self.uuid,
            'name': self.name
        }
