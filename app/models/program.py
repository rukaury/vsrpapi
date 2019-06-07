from neomodel import StructuredNode, StringProperty, UniqueIdProperty


class Program(StructuredNode):
    """
    Class to represent the Program node
    """
    uuid = UniqueIdProperty()
    name = StringProperty()
