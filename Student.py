import numpy as np

class Student():

	def __init__(self, course_transcript=None, classes_failed = None, classes_passed = None, semesters_completed=0, GPA=None, skill_level = 1, plan_to_retake = None, student_id = 0, is_minor=False):
		self.student_id = student_id #for printing purposes
		self.GPA = GPA
		self.course_transcript = {} if course_transcript == None else course_transcript
		self.semesters_completed = semesters_completed
		self.classes_failed = {} if classes_failed == None else classes_failed
		self.skill_level = skill_level
		self.plan_to_retake = [] if plan_to_retake == None else plan_to_retake
		self.failed_class_this_semester=False
		self.is_minor = is_minor

	def add_course_grade(self, course_id, grade):
		if grade < .7:
			self.classes_failed.setdefault(course_id, 0)
			self.classes_failed[course_id] += 1
			self.failed_class_this_semester = True

		#set self.course_transcript[course_id] to be grade
		if self.course_transcript.setdefault(course_id, grade) != grade:
			self.course_transcript[course_id] = grade



	def calculate_GPA(self):
		total_grades = 0
		if len(self.course_transcript) is 0:
			return None

		for i in range(len(self.course_transcript)):
			credit_points = 4
			if self.course_transcript[i] < .7:
				credit_points = 1
			elif self.course_transcript[i] < .8:
				credit_points = 2
			elif self.course_transcript[i] < .9:
				credit_points = 3


			total_grades += credit_points

		total_grades /= (len(self.course_transcript) * 4)
		return self.GPA

	def pass_rate(self):
		return 1 - float(self.classes_failed) / self.classes_taken
