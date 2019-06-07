from flask import make_response, jsonify
from app import app
from app.models.program import Program
from app.models.user import User
from neomodel import DoesNotExist


def response_for_program(program):
    """
    Return the response for when a single program was requested by the user.
    :param program:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'program': program
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

def get_programs_json_list(all_programs):
    """
    Make json objects of the user programs and add them to a list.
    :param all_programs: Program
    :return:
    """
    programs = []
    for program in all_programs:
        programs.append(program.json())
    return programs

def get_programs():
    """
    Get a list of all programs
    :return: programs.
    """
    items = None
    try:
        return Program.nodes.all()
    except DoesNotExist:
        return None

def response_for_programs_list(all_programs):
    """
    Return the response for when a single event was requested by the user.
    :param event:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'programs': all_programs
    }))

def get_single_program(program_id):
    try:
        program = Program.nodes.get(uuid=program_id)
        return program
    except DoesNotExist:
        return None



