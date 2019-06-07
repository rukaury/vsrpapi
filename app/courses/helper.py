from app.models.course import Course
from app.models.school import School
from neomodel import DoesNotExist
from functools import wraps
from flask import jsonify, make_response, request, url_for


def school_required(f):
    """
    Decorator to ensure that a valid school id is sent in the url path parameters
    :param f:
    :return:
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        school_id = request.view_args['school_id']
        try:
            str(school_id)
        except ValueError:
            return response('failed', 'Provide a valid School Id', 401)
        return f(*args, **kwargs)
    return decorated_function


def response_for_course(course):
    """
    Return the response for when a single course was requested by the user.
    :param course:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'course': course
    }))


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


def get_courses_json_list(all_courses):
    """
    Make json objects of the school's courses and add them to a list.
    :param all_courses: Course
    :return:
    """
    courses = []
    for course in all_courses:
        courses.append(course.json())
    return courses


def response_for_courses_list(all_courses):
    """
    Return the response for when courses are requested by the user.
    :param courses:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'courses': all_courses
    }))


def get_school(school_id):
    '''
    Get a school by its id
    :param school_id: School
    :return school
    '''
    school = None
    try:
        school = School.nodes.get(uuid=school_id)
        return school
    except DoesNotExist:
        return None
