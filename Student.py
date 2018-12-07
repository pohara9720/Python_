# a class must have an init function and take in self and the arugements of your class
#object parameter can be used to take in another object to inherit it inside your new class 

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,major,gpa,is_passing,classes):
		super(Student, self).__init__()
		self.name = name
		self.major = major
		self.gpa = gpa
		self.is_passing = is_passing
		self.classes = classes

	def on_honor_roll(self):
		if self.gpa >= 3.5:
			return True
		else:
			return False

class Question(object):
	"""docstring for Question"""
	def __init__(self, p,a):
		super(Question, self).__init__()
		self.prompt = p
		self.answer = a


