class student(objet):
  student_count = 0

def __new__(self):
  print('student .__new__')

def __inint__(self):
  print('student.__new__')
  self.gpa = 4.00

def study_hard(self):
  print('sir, yes sir.')
