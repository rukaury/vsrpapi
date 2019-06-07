'''

from app.models.neomodels import Quiz, Room


def create_quiz(name, room_id):
    room = Room.nodes.get_or_none(uuid=room_id)
    if room is None:
        raise ValueError("Room with id " + room_id + " does not exist")
        return
    new_quiz = Quiz(name=name)
    new_quiz.save()
    new_quiz.asked_in.connect(room)


def get_quiz(quiz_id):
    quiz = Quiz.nodes.get_or_none(uuid=quiz_id)
    if room is None:
        raise ValueError("Quiz with id " + quiz_id + " cannot be found")
    return room
'''