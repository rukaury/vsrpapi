from flask import make_response, jsonify
from app import app
from app.models.school import School
from app.models.user import User
from neomodel import DoesNotExist


def response_for_school(school):
    """
    Return the response for when a single school was requested by the user.
    :param school: School
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'school': school
    }))

def response(status, message, code):
    """
    Helper method to make a http response
    :param status: Status message
    :param message: Response message
    :param code: Response status code
    :return: Http Response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), code

def get_schools_json_list(all_schools):
    """
    Make json objects of the user schools and add them to a list.
    :param all_schools: School
    :return:
    """
    schools = []
    for school in all_schools:
        schools.append(school.json())
    return schools

def get_schools():
    """
    Get a list of all schools
    :return: School
    """
    items = None
    try:
        return School.nodes.all()
    except DoesNotExist:
        return None

def response_for_schools_list(all_schools):
    """
    Return the response for when a single event was requested by the user.
    :param schools: School
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'schools': all_schools
    }))

def get_single_school(school_id):
    """
    Return a single school.
    :param school_id: integer
    :return: School
    """
    try:
        school = School.nodes.get(uuid=school_id)
        return school
    except DoesNotExist:
        return None



