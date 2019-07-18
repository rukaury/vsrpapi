from app.room.helper import (response, get_course_from_user, create_and_save_room, response_for_created_room, response_for_created_question,
                             check_user_is_room_admin, get_single_room, get_all_rooms, response_for_rooms_list, response_for_single_room, get_questions_for_room, create_and_save_question, get_single_question, get_answers_for_question, response_for_single_question_with_answers, room_required, add_users_to_room, response_for_added_users, question_required, add_answer_to_user, response_for_associated_answer)
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


@rooms.route('/rooms/<room_id>/questions', methods=['POST'])
@token_required
@room_required
def create_question(current_user, room_id):
    """
    Create an room from the sent json data.
    :param current_user: Current User
    :return:
    """
    room = get_single_room(current_user, room_id)
    if not room:
        return response('failed', 'Room matching ID not found', 400)

    if request.content_type == 'application/json':
        data = request.get_json().get("question")
        title = data.get('title') if data.get('title') is not None else None
        text = data.get('text') if data.get('text') is not None else None
        is_mcq = data.get('is_mcq') if data.get('is_mcq') is not None else None
        answers = data.get('answers') if data.get(
            'answers') is not None else None

        if title and text:
            user_question = create_and_save_question(
                title, text, is_mcq, answers, room)
            return response_for_created_question(user_question, 201)
        return response('failed', 'Missing some room data, nothing was changed', 400)
    return response('failed', 'Content-type must be json', 202)


@rooms.route('/rooms/<room_id>/questions/<question_id>/answers/<answer_id>', methods=['POST'])
@token_required
@room_required
@question_required
def associate_answer_to_user(current_user, room_id, question_id, answer_id):
    """
    Asscoiate an answer with a user from the sent json data.
    :param current_user: Current User
    :param answer_id: answer id
    :return:
    """
    room = get_single_room(current_user, room_id)
    if not room:
        return response('failed', 'Room matching ID not found', 400)

    question = get_single_question(room, question_id)
    if not question:
        return response('failed', 'Question matching ID not found', 400)

    user_answer = add_answer_to_user(current_user, answer_id)
    if not user_answer:
        return response('failed', 'Answer matching ID not found', 400)

    return response_for_associated_answer(user_answer, 201)

@rooms.route('/rooms/<room_id>/invite', methods=['POST'])
@token_required
@room_required
def add_users(current_user, room_id):
    """
    Create a relationship between users and room.
    :param current_user: Current User
    :param room_id: Room id
    :return:
    """
    room = get_single_room(current_user, room_id)

    if not room:
        return response('failed', 'Room matching ID not found', 400)

    if room.admin.single().username != current_user.username:
        return response('failed', 'User is not room admin', 403)

    if request.content_type == 'application/json':
        users = request.get_json().get("users")

        if users:
            added_users = add_users_to_room(users, room)
            return response_for_added_users(added_users, 201)
        return response('failed', 'Missing some users data, nothing was changed', 400)
    return response('failed', 'Content-type must be json', 202)


@rooms.route('/rooms', methods=['GET'])
@token_required
def view_all_rooms(current_user):
    rooms_json = get_all_rooms(current_user)
    return response_for_rooms_list(rooms_json)


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
        return response('failed', "Room not found", 404)

    questions = get_questions_for_room(room)

    return response_for_single_room(room, questions)


@rooms.route('/rooms/<room_id>/questions/<question_id>', methods=['GET'])
@token_required
@room_required
def view_question_with_answer(current_user, room_id, question_id):
    """
    Get the room from the graph
    :param room_id: the uuid of the room to get
    :param current_user: Current User
    :return: the room matching the id
    """
    try:
        str(question_id)
    except ValueError:
        return response('failed', 'Please provide a valid room id', 400)

    room = get_single_room(current_user, room_id)

    if not room:
        return response('failed', "Room not found", 404)

    question = get_single_question(room, question_id)

    if not question:
        return response('failed', "Question not found", 404)

    answers = get_answers_for_question(current_user, question)

    return response_for_single_question_with_answers(question, answers)


@rooms.route('/rooms/<room_id>', methods=['PUT'])
@token_required
@room_required
def edit_room(current_user, room_id):
    """
    Validate the room Id. Also check for the data in the json payload.
    If the data exists update the room with the new data.
    :param current_user: Current User
    :param room_id: room Id
    :return: Http Json response
    """
    if request.content_type == 'application/json':
        data = request.get_json().get("room")
        name = data.get('name') if data.get("name") is not None else None
        course_code = data.get('course_code') if data.get(
            "course_code") is not None else None
        course = None

        if name or course_code:
            # Get a course from user school
            if course_code:
                course = get_course_from_user(current_user, course_code)
                if not course:
                    return response('failed', 'User is not allowed to participate in rooms with course code' + course_code, 404)

            # Check if user is admin of the room
            check = check_user_is_room_admin(current_user, room_id)

            if not check:
                return response('failed', 'Forbidden', 403)

            # Check the room we want to update
            user_room = get_single_room(current_user, room_id)

            if not user_room:
                abort(404)

            rel = user_room.admin.relationship(current_user)
            user_room.update(name, course, rel)
            return response_for_created_room(user_room, 201)
        return response('failed', 'No attribute or value was specified, nothing was changed', 400)
    return response('failed', 'Content-type must be json', 202)


@rooms.route('/rooms/<room_id>', methods=['DELETE'])
@token_required
@room_required
def delete_room(current_user, room_id):
    """
    Deleting a User room from the database if it exists.
    :param current_user:
    :param room_id:
    :return:
    """
    # Check if user is admin of the room
    check = check_user_is_room_admin(current_user, room_id)

    if not check:
        return response('failed', 'Forbidden', 403)

    # Check the room we want to update
    user_room = get_single_room(current_user, room_id)

    if not user_room:
        abort(404)

    user_room.delete()
    return response('success', 'Room Deleted successfully', 200)


@rooms.errorhandler(404)
def handle_404_error(e):
    """
    Return a custom message for 404 errors.
    :param e:
    :return:
    """
    return response('failed', 'Room resource cannot be found', 404)


@rooms.errorhandler(400)
def handle_400_errors(e):
    """
    Return a custom response for 400 errors.
    :param e:
    :return:
    """
    return response('failed', 'Bad Request', 400)
