from app.room.helper import (get_course_from_user, create_and_save_room,
                             response_for_created_room, get_single_room, response_for_single_room, get_all_rooms, response_for_rooms_list, response_for_rooms_quizzes)
from flask import Blueprint, request, abort
from app.auth.helper import token_required

# Initialize blueprint
rooms = Blueprint('room', __name__)


@rooms.route('/rooms/', methods=['POST'])
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
        course_code = data.get('course_code') if data.get(
            'course_code') is not None else None
        if name and course_code:
            course = get_course_from_user(current_user, course_code)
            if not course:
                return response('failed', 'User is not registered to course with code ' + course_code, 400)
            user_room = create_and_save_room(name, True, current_user, course)
            return response_for_created_room(user_room, 201)
        return response('failed', 'Missing some room data, nothing was changed', 400)
    return response('failed', 'Content-type must be json', 202)


@rooms.route('/rooms/<room_id>', methods=['GET'])
@token_required
def view_single_room(current_user, room_id):
    """
    Get the room from the graph
    :param room_id: the uuid of the room to get
    :param current_user: Current User
    :return: the room matching the id
    """
    try:
        str(room_id)
    except ValueError:
        return response('failed', 'Please provide a valid room id', 400)
    room = get_single_room(current_user, room_id)
    if not room:
        return response('failed', "Program not found", 404)
    return response_for_single_room(room)


@rooms.route('/rooms/', methods=['GET'])
@token_required
def view_all_rooms(current_user):
    rooms_json = get_all_rooms(current_user)
    return response_for_rooms_list(rooms_json)


@rooms.route('/rooms/<room_id>/quizzes/', methods=['GET'])
@token_required
def view_rooms_quizzes(current_user, room_id):
    """
    Get the room from the graph
    :param room_id: the uuid of the room to get
    :param current_user: Current User
    :return: the room matching the id
    """
    try:
        str(room_id)
    except ValueError:
        return response('failed', 'Please provide a valid room id', 400)
    room = get_single_room(current_user, room_id)
    if not room:
        return response('failed', "Program not found", 404)

    quizzes = room.quizzes

    return response_for_rooms_quizzes(room, quizzes)
