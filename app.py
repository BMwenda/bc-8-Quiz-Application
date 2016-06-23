import cmd

import actions

class QuizzApp(cmd.Cmd):

    width = actions.get_terminal_width() # get the size of the terminal

    intro = actions.draw_static_screen(width)
    prompt = "(quizme)"

    def do_listquizzes(self, args):
        """List all quizes in the local library."""
        for quiz in actions.list_quizzes():
            print(quiz)

    def do_importquiz(self, path_to_quiz):
        """Import a quiz to the local library."""
        actions.import_quiz(path_to_quiz)

    def do_takequiz(self, quiz_name):
        """Take a quiz."""
        actions.draw_static_screen(actions.get_terminal_width())
        actions.take_quiz(quiz_name)

    def do_download(self, quiz_name):
        """Download a quiz from the online repository."""
        actions.download_quiz(quiz_name)

    def do_upload(self, quiz_name):
        """Upload a quiz to the online repository."""
        actions.upload_quiz(quiz_name)

    def do_online_quizes(self):
        """List all quizzes in the online repository."""
        actions.list_online_quizzes()


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