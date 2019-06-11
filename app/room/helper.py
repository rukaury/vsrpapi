from app.models.room import Room
from app.models.answer import Answer
from app.models.question import Question
from flask import make_response, jsonify

def room_required(f):
    """
    Decorator to ensure that a valid room id is sent in the url path parameters
    :param f:
    :return:
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        event_id = request.view_args['room_id']
        try:
            str(room_id)
        except ValueError:
            return response('failed', 'Provide a valid Room Id', 401)
        return f(*args, **kwargs)

    return decorated_function

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


def create_and_save_question(title, text, is_mcq, answers, room):
    '''
    Helper to create a question and save it to the graph
    :param name: the name of the question
    :param active: whether or not this question will be active by default
    :param admin_id: the user id representing the admin
    :param course_id: the course code / id representing the course that this question studies
    :return ValueError: raised if either the course or user cannot be found in the graph
    '''

    new_question = Question(title=title, text=text, is_multiple_choice=is_mcq)
    new_question.save()

    new_question.room.connect(room)

    # def process_answers()
    for a in answers:
        temp_answ = Answer(text=a.get('text'), correct=a.get('correct'))
        temp_answ.save()
        temp_answ.question.connect(new_question)

    return new_question


def get_course_from_user(current_user, course_code):
    '''
   Helper to retrieve a course from a user
   :param current_user: the current user
   :param course_code: the code matching the code of the course in the graph
   :return course: the course matching the course_code
   '''
    return current_user.school.get().courses.get_or_none(code=course_code)


def get_single_room(current_user, room_id):
    '''
    Helper to retrieve a room from the graph using a room id
    :param room_id: the id matching the uuid of the room in the graph
    :return room: the room matching the room_id
    '''
    return current_user.rooms.get_or_none(uuid=room_id)


def check_user_is_room_admin(current_user, room_id):
    '''
   Helper to check if a room admin is the current user
   :param room_id: the id matching the uuid of the room in the graph
   :return bool: Boolean
   '''
    return Room.nodes.get_or_none(uuid=room_id).admin.get().username == current_user.username


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


def get_single_question(room, question_id):
    '''
    Helper to retrieve a question from the graph using a question id
    :param room: the room to get the question from
    :param question_id: the id matching the uuid of the question in the graph
    :return question: the question matching the question_id
    '''
    return room.questions.get_or_none(uuid=question_id)


def get_questions_for_room(room):
    """
    Get the questions for a given room
    :param room: neomodel room with questions 
    :return questions[]: array of questions
    """
    questions_array = []
    questions = room.questions
    for q in questions:
        questions_array.append(q.json())
    return questions_array


def get_answers_for_question(question):
    """
    Get the answers for a given question
    :param question: neomodel room with answers 
    :return answers[]: array of answers
    """
    answers_array = []
    answers = question.answers

    for a in answers:
        answers_array.append(a.json())
    return answers_array


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


def response_for_created_question(question, status_code):
    """
    Method returning the response when an room has been successfully created.
    :param status_code:
    :param room: room
    :return: Http Response
    """
    return make_response(jsonify({'room': {
        'uuid': question.uuid,
        'title': question.title,
        'text': question.text,
        'is_mcq': question.is_multiple_choice
    }, 'status': 'success'})), status_code


def response_for_single_room(room, questions):
    room_with_questions = {
        "name": room.name,
        "active": room.active,
        "room_id": room.uuid,
        "questions": questions
    }

    return make_response(jsonify(room_with_questions))


def response_for_single_question_with_answers(question, answers):
    question_with_answers = {
        "title": question.title,
        "text": question.text,
        "is_mcq": question.is_multiple_choice,
        "answers": answers
    }

    return make_response(jsonify(question_with_answers))
