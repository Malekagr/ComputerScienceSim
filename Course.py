import numpy as np
import math
import random

class Course():

	#term is 1 for odd, 2 for even, 3 for all
	def __init__(self, course_id, is_core =True, class_size=float('inf'), students=None, difficulty=0, term=3, requirements = None):
		self.course_id = course_id
		self.class_size = class_size
		self.students = [] if students == None else students
		self.waitlist = []
		self.difficulty = difficulty
		self.term = term
		self.is_core = is_core
		self.requirements = [] if requirements == None else requirements
