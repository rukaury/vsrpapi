from app import app, bcrypt
from .blacklist_token import BlackListToken
from neomodel import (StructuredNode, StringProperty, DateTimeProperty, RelationshipTo, One, DoesNotExist)
from app.models.relationships.base_rel import BaseRel
import datetime
import jwt
import pytz


class User(StructuredNode):
    """
    Class to represent the User node
    """
    username = StringProperty(unique=True, required=True)
    f_name = StringProperty(required=True)
    l_name = StringProperty(required=True)
    password = StringProperty(required=True)
    registered_on = DateTimeProperty(default_now=True, format='%Y-%m-%d %H:%M')

    # traverse outgoing TAKES relationship, inflate Program that the user is enrolled in
    program = RelationshipTo('app.models.program.Program', 'TAKES', cardinality=One, model=BaseRel)
    # traverse outgoing ATTENDS relationship, inflate School that user goes to
    school = RelationshipTo('app.models.school.School', 'ATTENDS', cardinality=One, model=BaseRel)

    def save_user(self):
        """
        Persist the user in the database
        :param user:
        :return:
        """
        self.password = bcrypt.generate_password_hash(self.password, app.config.get('BCRYPT_LOG_ROUNDS')) \
            .decode('utf-8')
        self.save()
        return self.encode_auth_token(self.username)

    def encode_auth_token(self, username):
        """
        Encode the Auth token
        :param username: username
        :return:
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=app.config.get('AUTH_TOKEN_EXPIRY_DAYS'),
                                                                       seconds=app.config.get(
                                                                           'AUTH_TOKEN_EXPIRY_SECONDS')),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(
                payload,
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token):
        """
        Decoding the token to get the payload and then return the user Id in 'sub'
        :param token: Auth Token
        :return:
        """
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            is_token_blacklisted = BlackListToken.check_blacklist(token)
            if is_token_blacklisted:
                return 'Token was Blacklisted, Please login In'
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired, Please sign in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please sign in again'

    @staticmethod
    def get_by_username(username):
        """
        Check a user by their username
        :param username:
        :return:
        """
        try:
            return User.nodes.get(username=username)
        except DoesNotExist:
            return None
        

    def reset_password(self, new_password):
        """
        Update/reset the user password.
        :param new_password: New User Password
        :return:
        """
        self.password = bcrypt.generate_password_hash(new_password, app.config.get('BCRYPT_LOG_ROUNDS')) \
            .decode('utf-8')
        self.save()
        
    
