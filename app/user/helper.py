from app.models.user import User
from neomodel import DoesNotExist
from functools import wraps
from flask import jsonify, make_response, request, url_for


def response(status, message, http_code):
    """
    Helper method to make a http response
    :param status: Status message
    :param message: Response message
    :param http_code: Response status http_code
    :return: Http Response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), http_code


def get_usernames_list():
    """
    Make an array of users usernames and add them to a list.
    :param all_users: User
    :return:
    """
    users = User.nodes.all();
    usernames = [];
    for user in users:
        usernames.append(user.username)
    return usernames


def response_for_users_list(all_users):
    """
    Return the response for all users.
    :param all_users: User[]
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'users': all_users
    }))