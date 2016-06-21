import json
from question import Question

def load_questions(quiz_file):
	"""This function loads questions from a quiz(in json format).
	   Returns a list of Question objects.
	"""
	data = open(quiz_file,"r").read()
	quiz = json.loads(data)
	questions = []
	for question in quiz["questions"]:
		text = question["question_text"]
		answer = question["answer"]
		try:
			#some questions may be open endend and thus may not have choices
			choices = question["choices"]
		except KeyError:
			choices = None
		questions.append(Question())
	return questions

questions = load_questions("testquiz.json")
print(questions)






