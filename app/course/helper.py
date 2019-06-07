'''

def create_course(code, school_id):
    school = School.nodes.get_or_none(uuid=school_id)
    if school is None:
        raise ValueError("School with id " + school_id + " does not exist")
        return
    new_course = Course(code=code)
    new_course.save()

    new_course.taught_at.connect(school)

'''
