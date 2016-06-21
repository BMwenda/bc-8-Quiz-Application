import json
from question import Question
from shutil import copyfile


def load_questions(quiz_file):
    """Load questions from a quiz file. Return a list of questions."""
    data = open(quiz_file, "r").read()
    quiz = json.loads(data)
    questions = []
    for question in quiz["questions"]:
        text = question["question_text"]
        answer = question["answer"]
        try:
            # some questions may be open endend and thus may not have choices
            choices = question["choices"]
        except KeyError:
            choices = None
        questions.append(Question(text, answer, choices))
    return questions


def import_quiz(path_to_quiz):
    """Import a quiz file to the quiz library."""
    quiz_name = json.loads(open(path_to_quiz).read())["name"]
    copyfile(path_to_quiz, "quizzes/" + quiz_name)

# questions = load_questions("quizzes/testquiz.json")
# for question in questions:
#    print(question.question_text)
#import_quiz("/home/bit_chef/Desktop/math_quiz.json")
