from app.models import user, program, school


def create_user(username, f_name, l_name, password, school_id, program_id):
    program = Program.nodes.get_or_none(uuid=program_id)
    school = School.nodes.get_or_none(uuid=school_id)
    if program or school is None:
        raise ValueError("Program or School Does Not Exist!")
        return
    new_user = User(username=username,  f_name=f_name,
                    l_name=l_name, password=password)
    new_user.save()
    new_user.attending.connect(school)
    new_user.studying.connect(program)
