from .helper_room import response_all_rooms, response_single_room
from flask import Blueprint, request, abort
from app.auth.helper import token_required

# Initialize blueprint
rooms = Blueprint('room', __name__)


@rooms.route('/rooms', methods=['GET'])
def view_all_rooms():
    """
    Return all rooms
    """
    return response_all_rooms()


@rooms.route('/rooms/<room_id>', methods=['GET'])
def view_single_rooms(room_id):
    """
    Return a single room, matching argument
    :param room_id: the room ID to lookup
    """
    return response_single_room(room_id)
