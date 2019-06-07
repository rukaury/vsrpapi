from flask import Blueprint, request
from app.courses.helper import (get_school, school_required, response, response_for_courses_list, get_courses_json_list)

# Initialize blueprint
courses = Blueprint('courses', __name__)


@courses.route('/schools/<school_id>/courses', methods=['GET'])
@school_required
def courselist(school_id):
    """
    Return all the courses for a school.
    Return an empty courses object if no course
    Return a 404 if school does not exist
    :return:
    """
    school = get_school(school_id)
    if school is None:
        return response("failed", "School with id " + school_id + " does not exist", 404)

    courses = school.courses
    items = []

    if(len(courses)):
        for c in courses:
            items.append(c)


    #print(items, school)

    if items:
        return response_for_courses_list(get_courses_json_list(items))
    return response_for_courses_list([])
