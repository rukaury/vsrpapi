from neomodel import StructuredNode, StringProperty, UniqueIdProperty


class Program(StructuredNode):
    """
    Class to represent the Program node
    """
    uuid = UniqueIdProperty()
    name = StringProperty(required=True)

    def update(self, name, rel):
        """
        Function will update the name of the program
        :param name: the name of the program
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
           
