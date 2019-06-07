from neomodels import (Program, School, User, Course,
                       Room, Quiz, Question, Answer)


def create_school(name):
    new_school = School(name=name)
    new_school.save()


def create_program(name):
    new_program = Program(name=name)
    new_program.save()


def create_answer(text, is_correct_answer, question_id):
    question = Question.nodes.get_or_none(question_id)
    if question is None:
        raise ValueError("Question with id " + question_id + " does not exist")
        return

    new_answer = Answer(text=text, correct=is_correct_answer)
    new_answer.save()
    new_answer.answer_for.connect(question)
