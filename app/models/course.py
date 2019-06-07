from neomodel import StructuredNode, StringProperty, RelationshipTo


class Course(StructuredNode):
    """
    Class to represent the Course node
    """
    code = StringProperty(unique_index=True)

    # traverse outgoing TAUGHT_AT relationship, inflate School the course is taught at
    taught_at = RelationshipTo(School, 'TAUGHT_AT')

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
