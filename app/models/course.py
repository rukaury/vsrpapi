from neomodel import StructuredNode, StringProperty, RelationshipTo


class Course(StructuredNode):
    """
    Class to represent the Course node
    """
    code = StringProperty(unique_index=True)

    # traverse outgoing TAUGHT_AT relationship, inflate School the course is taught at
    taught_at = RelationshipTo(School, 'TAUGHT_AT')
