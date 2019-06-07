import datetime
from flask import Blueprint, request, abort
from app.auth.helper import token_required
from app.programs.helper import response, response_for_program, get_programs_json_list, response_for_programs_list, get_programs, get_single_program
from app.models.user import User
from app.models.program import Program
from neomodel import DoesNotExist

# Initialize blueprint
programs = Blueprint('programs', __name__)


@programs.route('/programs', methods=['GET'])
def programlist():
    """
    Return all the programs.
    Return an empty programs object if no programs
    :return:
    """
    items = get_programs()

    if items:
        return response_for_programs_list(get_programs_json_list(items))
    return response_for_programs_list([])

@programs.route('/programs/<program_id>', methods=['GET'])
def get_program(program_id):
    """
    Return a program.
    :param program_id: Program Id
    :return:
    """
    try:
        str(program_id)
    except ValueError:
        return response('failed', 'Please provide a valid Event Id', 400)
    else:
        program = get_single_program(program_id)
        if program:
            return response_for_program(program.json())
        else:
            return response('failed', "Program not found", 404)

@programs.route('/user/programs', methods=['GET'])
@token_required
def get_user_program(current_user):
    """
    Return a program.
    :param program_id: Program Id
    :return:
    """
    user_program = User.get_by_username(current_user.username).program
    if user_program:
        return response_for_program(user_program.json())
    else:
        return response('failed', "User program not found", 404)
            