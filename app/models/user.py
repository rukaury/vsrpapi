from neomodel import StructuredNode, StringProperty, DateProperty, RelationshipTo


class User(StructuredNode):
    """
    Class to represent the User node
    """
    username = StringProperty(unique_index=True)
    f_name = StringProperty()
    l_name = StringProperty()
    password = StringProperty()
    created_on = DateProperty(default_now=True)

    # traverse outgoing TAKES relationship, inflate Program that the user is enrolled in
    studying = RelationshipTo(Program, 'TAKES')
    # traverse outgoing ATTENDS relationship, inflate School that user goes to
    attending = RelationshipTo(School, 'ATTENDS')
