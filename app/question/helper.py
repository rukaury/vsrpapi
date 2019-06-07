'''

from app.models.neomodels import Quiz, Question


def create_question(title, text, is_multi, quiz_id):
    quiz = Quiz.nodes.get_or_none(uuid=quiz_id)
    if quiz is None:
        raise ValueError("Quiz with id " + quiz_id + " does not exist")
        return
    new_question = Question(title=title, text=text,
                            is_multiple_choice=is_multi)
    new_question.save()
    new_question.asked_by.connect(quiz)

'''
