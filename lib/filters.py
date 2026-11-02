# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
  """
  Return a filtered list of students by major using a list comprehension.
  The function should:
  - Check if a student's major matches the given major (case insensitive).
  - Return a new list containing only students that match.
  """
  # for student in student_list -> examines each student tuple
  # student[2] -> accesses the student's major (the third element of the tuple)
  # if student[2].lower() == major.lower() -> checks if the student's major matches the given major (case insensitive)
  # return [...] -> returns new list containing the matches 
  return [student for student in student_list if student[2].lower() == major.lower()]

