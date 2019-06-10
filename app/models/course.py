from neomodel import StructuredNode, StringProperty, RelationshipTo, One
from app.models.relationships.base_rel import BaseRel

class Course(StructuredNode):
    """
    Class to represent the Course node
    """
    code = StringProperty(unique=True, unique_index=True)

    # traverse outgoing TAUGHT_AT relationship, inflate School the course is taught at
    school = RelationshipTo("app.models.school.School", 'TAUGHT_AT', cardinality=One, model=BaseRel)

    def update(self, code, rel):
        """
        Function will update the course
        :param code: the new course code
        """

        self.code = code if code is not None else self.code
        rel.updated_on = datetime.datetime.now()
        self.save()

    def json(self):
        """
        Json representation of the course model.
        :return code: the course code
        """
        return {
            'code': self.code
        }
