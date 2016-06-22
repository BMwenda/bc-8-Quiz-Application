import json
import os
from question import Question
from shutil import copyfile


def load_questions(quiz_file):
    """Load questions from a quiz file. Return a list of questions."""
    quiz_file = "quizzes/" + quiz_file + ".json"
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
    copyfile(path_to_quiz, "quizzes/" + quiz_name + ".json")


def list_quizzes():
    """List all quizzes in the library."""
    quiz_files = [file.replace(".json", "") for file in os.listdir("quizzes")]
    return quiz_files


def take_quiz(quiz_file):
    """Take the a quiz."""
    try:
        questions = load_questions(quiz_file)
    except IndexError:
        print("{} does not exist on the Quiz Library".format(quiz_file))
        return
    graded_answers = []
    for question in questions:
        print(question.to_string())
        user_answer = input("Answer: ")
        graded_answers.append(question.grade(user_answer))
        os.system("clear")
    #summary
    print("           SUMMARY")
    print("Total questions attempted: {}".format(len(graded_answers)))
    print("Correct attempts:   {}".format(graded_answers.count(True)))
    print("Incorrect attempts: {}".format(graded_answers.count(False)))


#questions = load_questions("quizzes/testquiz.json")
#for question in questions:
#    print(question.to_string())
# for question in questions:
#    print(question.question_text)
# import_quiz("/home/bit_chef/Desktop/math_quiz.json")
# print(list_quizzes())