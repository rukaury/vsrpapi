from neomodel import config


if __name__ == "__main__":
    config.DATABASE_URL = 'bolt://flask:password@127.0.0.1:7687'
    """
    # Make a program
    pr = Program(name="Physics")
    pr.save()
    # Make a school
    sc = School(name="University of Ottawa")
    sc.save()
    # Make a class / course
    cl = Course(code="CS-101")
    cl.save()
    cl.taught_at.connect(sc)
    # make a user
    us = User(username="admin", f_name="first",
              l_name="last", password="secret")
    us.save()
    us.attending.connect(sc)
    us.studying.connect(pr)

    # make a room
    ro = Room(name="Study Room", active=True)
    ro.save()
    ro.participant.connect(us)
    ro.admin.connect(us)
    ro.studies.connect(cl)
    """
    ro = Room.nodes.get_or_none(uuid="70aabcb6a68242cfadff2d32fb63f553")

    # Make a quiz
    quiz = Quiz(name="Exam Review")
    quiz.save()
    quiz.asked_in.connect(ro)

    # make some questions
    for i in range(0, 4):
        question = Question(title="Qestion_Title_" + str(i),
                            text="Question_Test_" + str(i), is_multiple_choice=True)
        question.save()
        # make some answers
        correct = Answer(text="I'm Correct", correct=True)
        correct.save()
        correct.answer_for.connect(question)
        for i in range(1, 4):
            incorrect = Answer(text="I'm not correct", correct=False)
            incorrect.save()
            incorrect.answer_for.connect(question)
        question.asked_by.connect(quiz)
