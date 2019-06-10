from app.models.room import Room
from flask import make_response, jsonify


def create_and_save_room(name, active, admin_id, course_id):
    '''
    Helper to create a room and save it to the graph
    :param name: the name of the room
    :param active: whether or not this room will be active by default
    :param admin_id: the user id representing the admin
    :param course_id: the course code / id representing the course that this room studies
    :return ValueError: raised if either the course or user cannot be found in the graph
    '''
    course_it_studies = Course.nodes.get_or_none(uuid=course_id)
    admin = User.nodes.get_or_none(uuid=admin_id)
    if course_it_studies or admin is None:
        raise ValueError("Course or User Does Not Exist!")
        return
    new_room = Room(name=name, active=active)
    new_room.save()
    new_room.admin.connect(admin)
    new_room.participant.connect(admin)
    new_room.studies.connect(course_it_studies)


def get_room_by_id(room_id):
    '''
    Helper to retrieve a room from the graph using a room id
    :param room_id: the id matching the uuid of the room in the graph
    :return room: the room (formatted to json) matching the room_id
    :return ValueError: if the room id cannot be found raises this error
    '''
    room = Room.nodes.get_or_none(uuid=room_id)
    if room is None:
        raise ValueError("Room with id " + room_id + " cannot be found")
    return room.json()


def get_all_rooms():
    '''
    Helper function to return a list of all rooms in the graph
    :return room_array: an array of all rooms (formatted to json) in the graph, empty if none exist
    '''
    rooms = Room.nodes.all()
    room_array = []
    for room in rooms:
        room_array.append({"room": room.json()})
    return room_array


def response_single_room(room_id):
    """
    Function to create a flask response when requesting a single room
    :param room_id: the room to get from the graph
    :returns make_response with json representation of a room
    """
    room = {}
    try:
        room = get_room_by_id(room_id)
    except ValueError:
        #The room does not exist  - Error
        return make_response(jsonify(room), 404)
    return make_response(jsonify(room))


def response_all_rooms():
        """
    Function to create a flask response when requesting all rooms
    :returns make_response with json representation of an array of rooms
    """
    return make_response(jsonify(get_all_rooms()))
