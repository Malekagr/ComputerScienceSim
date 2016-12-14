class Faculty():

	def __init__(self, ID=None, courses=None, difficulty=0.0):
		self.ID = ID
		courses = [] if courses == None else courses
		self.courses = courses		# a list of course objects
		self.difficulty = difficulty
