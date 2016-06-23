import json
import os
import time
from firebase import firebase
import requests
from shutil import copyfile
from termcolor import cprint
from pyfiglet import figlet_format

from question import Question

firebase = firebase.FirebaseApplication('https://quizzapp-299a2.firebaseio.com/', None)

def load_quiz_info(quiz_file):
    """
    Load information from a quiz file.

    Return a tuple containing a list of questions and
    the time allocated for the quiz.
    """
    quiz_file = "quizzes/" + quiz_file + ".json"
    data = open(quiz_file, "r").read()
    quiz = json.loads(data)
    time_allocated = int(quiz["time_allocated"])
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
    return {"time_allocated": time_allocated, "questions": questions}


def import_quiz(path_to_quiz):
    """Import a quiz file to the quiz library."""
    quiz_name = json.loads(open(path_to_quiz).read())["name"]
    copyfile(path_to_quiz, "quizzes/" + quiz_name + ".json")


def list_quizzes():
    """List all quizzes in the library."""
    try:
        quiz_files = [file.replace(".json", "") for file in os.listdir("quizzes")]
        return quiz_files
    except FileNotFoundError:
        os.mkdir()
        return []   # return empty list since no quizzes are available


def take_quiz(quiz_file):
    """Take the a quiz."""
    try:
        if quiz_file == "":
            print("You did not specify the quiz you want to take\n\
                To see the available quizzes, use the 'listquizzes command.")
            return
        quiz_info = load_quiz_info(quiz_file)
    except FileNotFoundError:
        print("{} does not exist on the Quiz Library".format(quiz_file))
        return

    questions = quiz_info["questions"]
    time_allocated = quiz_info["time_allocated"]
    graded_answers = []

    print("Time allocated for the quiz: {}".format(time_allocated))
    input("Press Enter to start the quiz. ")
    start_time = time.time()

    for question in questions:
        if time.time() - start_time > time_allocated:
            break
        draw_static_screen(get_terminal_width())
        print(question.to_string())
        user_answer = input("Answer: ")
        graded_answers.append(question.grade(user_answer))

    time_taken = time.time() - start_time

    # summary
    print("""
              SUMMARY
    Total questions attempted: {a}
    Correct attempts:          {b}
    Incorrect attempts:        {c}
    """.format(a=len(graded_answers),
               b=graded_answers.count(True),
               c=graded_answers.count(False)))

def download_quiz(quiz_name):
    """Download a quiz from the firebase repository."""
    quizzes = download_quizzes()
    desired_key = None
    for key in quizzes.keys():
        if quizzes[key]["name"] == quiz_name:
            desired_key = key
            break
    if desired_key is None:
        print("'{}' is not in the online repository".format(quiz_name))
        return None
    else:
        return quizzes[desired_key]


def list_online_quizzes():
    """List all quizzes stored in the firebase repository."""
    quizzes = download_quizzes()
    for key in quizzes.keys():
        print(quizzes[key]["name"])


def download_quizzes():
    """Download quizzes from online repository"""
    online_quizzes = firebase.get('/quizzapp-299a2/Quizzes', None)
    return online_quizzes


def draw_static_screen(width):
    """
    Draw the top part of the terminal screen.

    This part of the screen should not change whenever the
    program is running.
    """
    os.system("clear")
    cprint(" " * width, "green", "on_green", end="")
    cprint(figlet_format("quizme", justify="center", width=width))
    cprint("COMMANDS".center(width), attrs=["bold", "underline"])
    cprint("listquizzes -> List all quizes in the library.")
    cprint("onlinequiz  -> List all online quizzes")
    cprint("takequiz    <quiz name>     Take the a particular quiz.")
    cprint("importquiz  <path to quiz>  Import a quiz to the quiz library")


def get_terminal_width():
    """Return the width of the terminal"""
    try:
        width = os.get_terminal_size().columns
    except:
        #if any error occurs when getting the screen width, just use 70 as the width
        width = 70
    return width
