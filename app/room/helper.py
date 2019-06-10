from app.models.room import Room
from flask import make_response, jsonify


def create_and_save_room(name, active, user, course):
    '''
    Helper to create a room and save it to the graph
    :param name: the name of the room
    :param active: whether or not this room will be active by default
    :param admin_id: the user id representing the admin
    :param course_id: the course code / id representing the course that this room studies
    :return ValueError: raised if either the course or user cannot be found in the graph
    '''
    new_room = Room(name=name, active=active)
    new_room.save()
    new_room.admin.connect(user)
    user.rooms.connect(new_room)
    new_room.course.connect(course)
    return new_room


def get_course_from_user(user, course_code):
    return user.school.get().courses.get_or_none(code=course_code)


def get_single_room(current_user, room_id):
    '''
    Helper to retrieve a room from the graph using a room id
    :param room_id: the id matching the uuid of the room in the graph
    :return room: the room matching the room_id
    '''
    return current_user.rooms.get_or_none(uuid=room_id)


def get_all_rooms(current_user):
    '''
    Helper function to return a list of all rooms in the graph
    :return room_array: an array of all rooms (formatted to json) in the graph, empty if none exist
    '''
    rooms = current_user.rooms
    room_array = []
    for room in rooms:
        room_array.append(room.json())
    return room_array


def response_for_single_room(room):
    """
    Return the response for when a single room was requested by the user.
    :param program:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'room': room
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


def response_for_rooms_list(all_rooms):
    """
    Return the response when all rooms are requested.
    :param all_rooms:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'rooms': all_rooms
    }))


def response_for_created_room(room, status_code):
    """
    Method returning the response when an room has been successfully created.
    :param status_code:
    :param room: room
    :return: Http Response
    """
    return make_response(jsonify({'room': {
        'room_id': room.uuid,
        'room_name': room.name,
        'room_course': room.course.get().code
    }, 'status': 'success'})), status_code


def response_for_rooms_quizzes(room, quizzes):
    quiz_array = []
    if quizzes:
        for quiz in quizzes:
            quiz_array.append(quiz)

    room_with_quizzes = {
        "name": room.name,
        "active": room.active,
        "room_id": room.uuid,
        "quizzes": quiz_array
    }

    return make_response(jsonify(room_with_quizzes))
