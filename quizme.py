"""
quizme.

Usage:
    quizme.py listquizzes
    quizme.py importquiz <path>
    quizme.py takequiz  <quizname>

Options:
    -h --help   display this message
"""

from docopt import docopt
import actions


def main():
    """Entry point of the program."""
    arguments = docopt(__doc__)
    if arguments["listquizzes"]:
        for quiz in actions.list_quizzes():
            print(quiz)
    elif arguments["importquiz"]:
        actions.import_quiz(arguments["<path>"])
    elif arguments["takequiz"]:
        actions.take_quiz(arguments["<quizname>"])



if __name__ == '__main__':
    main()
