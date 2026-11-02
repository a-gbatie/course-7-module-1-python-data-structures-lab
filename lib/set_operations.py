# This module contains operations related to sets.

def unique_majors(student_list):
  """
  Return a set of unique student majors using set comprehension.
  Extract the major field from each student record.
  """
  return {student[2] for student in student_list} # student[2] gets the student's major -> for student in student_list loops through the students -> { } creates a set which automatically removes duplicates
