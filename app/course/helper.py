from app.models.course import Course


def response_for_course(course):
    """
    Return the response for when a single course was requested by the user.
    :param course:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'program': course
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


def get_courses():
    """
    Get a list of all courses
    :return: courses.
    """
    items = None
    try:
        return Course.nodes.all()
    except DoesNotExist:
        return None


'''

def create_course(code, school_id):
    school = School.nodes.get_or_none(uuid=school_id)
    if school is None:
        raise ValueError("School with id " + school_id + " does not exist")
        return
    new_course = Course(code=code)
    new_course.save()

    new_course.taught_at.connect(school)

'''
