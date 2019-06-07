from neomodel import (StructuredNode, StringProperty, DateTimeProperty)
from neomodel.exceptions import DoesNotExist
import datetime

class BlackListToken(StructuredNode):

    token = StringProperty(unique_index=True, unique=True)
    blacklisted_on = DateTimeProperty(default_now=True)

    def blacklist(self):
        """
        Persist Blacklisted token in the database
        :return:
        """
        self.save()

    @staticmethod
    def check_blacklist(token):
        """
        Check to find out whether a token has already been blacklisted.
        :param token: Authorization token
        :return:
        """
        try:
            response = BlackListToken.nodes.get(token=token)
            return True 
        except:
            return False