import datetime
from flask import Blueprint, request, abort
from app.auth.helper import token_required
from app.schools.helper import response, response_for_school, get_schools_json_list, response_for_schools_list, get_schools, get_single_school
from app.models.user import User
from app.models.school import School
from neomodel import DoesNotExist

# Initialize blueprint
schools = Blueprint('schools', __name__)


@schools.route('/schools', methods=['GET'])
def schoollist():
    """
    Return all the schools.
    Return an empty schools object if no schools
    :return:
    """
    items = get_schools()

    if items:
        return response_for_schools_list(get_schools_json_list(items))
    return response_for_schools_list([])

@schools.route('/schools/<school_id>', methods=['GET'])
def get_school(school_id):
    """
    Return a school.
    :param school_id: school Id
    :return:
    """
    try:
        str(school_id)
    except ValueError:
        return response('failed', 'Please provide a valid Event Id', 400)
    else:
        school = get_single_school(school_id)
        if school:
            return response_for_school(school.json())
        else:
            return response('failed', "school not found", 404)

@schools.route('/user/schools', methods=['GET'])
@token_required
def get_user_school(current_user):
    """
    Return a school.
    :param school_id: school Id
    :return:
    """
    user_school = User.get_by_username(current_user.username).school
    if user_school:
        return response_for_school(user_school.json())
    else:
        return response('failed', "User school not found", 404)
            