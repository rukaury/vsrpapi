'''

from app.models.room import


def create_room(name, active, admin_id, course_id):
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


def get_room(room_id):
    room = Room.nodes.get_or_none(uuid=room_id)
    if room is None:
        raise ValueError("Room with id " + room_id + " cannot be found")
    return room


'''