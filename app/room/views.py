from app.room.helper import get_course_from_user, create_and_save_room, response_for_created_room
from flask import Blueprint, request, abort
from app.auth.helper import token_required

# Initialize blueprint
rooms = Blueprint('room', __name__)

@rooms.route('/rooms', methods=['POST'])
@token_required
def create_room(current_user):
    """
    Create an room from the sent json data.
    :param current_user: Current User
    :return:
    """
    if request.content_type == 'application/json':
        data = request.get_json().get("room")
        name = data.get('name') if data.get('name') is not None else None
        course_code = data.get('course_code') if data.get('course_code') is not None else None
        if name and course_code:
            course = get_course_from_user(current_user, course_code)
            if not course:
                return response('failed', 'User is not registered to course with code ' + course_code, 400)
            user_room = create_and_save_room(name, True, current_user, course)
            return response_for_created_room(user_room, 201)
        return response('failed', 'Missing some room data, nothing was changed', 400)
    return response('failed', 'Content-type must be json', 202)
