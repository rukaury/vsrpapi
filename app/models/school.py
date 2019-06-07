from neomodel import StructuredNode, StringProperty, UniqueIdProperty


class School(StructuredNode):
    """
    Class to represent the School node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
