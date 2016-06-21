class Question(object):
	"""This class models question objects"""
	def __init__(self, question_text, answer, choices):
		"""This method accepts the following mandatory arguments:
		question_type ->
		"""
		self.question_text = question_text
		self.answer = answer
		self.choices = choices

	def grade(self, user_answer):
		if self.answer.lower() == user_answer.lower():
			return True
		return False



