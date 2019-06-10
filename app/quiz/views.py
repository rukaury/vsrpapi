from app.room.helper import response
from flask import Blueprint, request, abort
from app.auth.helper import token_required


# Initialize blueprint
quiz = Blueprint('programs', __name__)


@quiz.route('/quiz/<quiz_id>', methods=['GET'])
@token_required
def view_single_quiz(current_user, quiz_id):
    """
    Get the quiz, it's corresponding questions and answers
    :param room_id: the uuid of the room to get
    :param current_user: Current User
    :return: the room matching the id
    """
    return response("error", "Resource Not Found", 404)
