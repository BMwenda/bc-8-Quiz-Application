"""
Usage:
    quizme listquizzes
    quizme importquiz <path>
    quizme takequiz  <quizname>

Options:
    -h --help   display this message
"""
import cmd

import actions

class QuizzApp(cmd.Cmd):

    width = actions.get_terminal_width() # get the size of the terminal

    intro = actions.draw_static_screen(width)
    prompt = "(quizme)"

    def do_listquizzes(self, args):
        """Run the listquizzes command."""
        for quiz in actions.list_quizzes():
            print(quiz)

    def do_importquiz(self, args):
        """Run the import quiz command."""
        actions.import_quiz(args)

    def do_takequiz(self, args):
        """Run the takequiz command."""
        actions.draw_static_screen(actions.get_terminal_width())
        actions.take_quiz(args)

    #To fix. This function is not currently working
    def complete_takequiz(self, text, line, begidx, endidx): 
        """Provide autocompletion of arguments of the takequiz command."""
        if not text:
            completions = actions.list_quizzes()
        else:
            completions = [quiz for quiz in actions.listquizzes() if quiz.startswith(text)]
        return completions

    def emptyline(self):
        """Redraw the static screen if no command is supplied."""
        actions.draw_static_screen(actions.get_terminal_width())

    def default(self, args):
        """Display a warning message when an invalid command is entered."""
        print("Invalid command")


if __name__ == "__main__":
    QuizzApp().cmdloop()