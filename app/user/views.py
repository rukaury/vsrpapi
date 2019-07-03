from flask import Blueprint, request
from app.user.helper import (response, response_for_users_list, get_usernames_list)

# Initialize blueprint
users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def userlist():
    """
    Return all the users.
    Return an empty users object if no users
    :return:
    """
    users = get_usernames_list()

    if users:
        return response_for_users_list(users)
    return response_for_courses_list([])
