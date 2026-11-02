# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
  """
  Generate student records filtered by major lazily for memory efficiency
  using a Python generator.
  """
  return (student for student in student_list if student[2].lower() == major.lower()) # student[2] gets the student's major -> for student in student_list loops through the students -> if student[2].lower() == major.lower() checks if the student's major matches the given major (case insensitive) -> ( ) creates a generator which yields one student at a time
