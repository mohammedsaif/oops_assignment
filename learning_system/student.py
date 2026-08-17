from parent import User
class Student(User):
        def __init__(self, name, email, userid):
                super().__init__(name, email, userid)
                self.enrolled_courses = {}

        def enroll_course(self,course):
                self.enrolled_courses[course.course_id] = {
                        "course":course,
                        "progress": 0
                }
                print(f"{self.name} enrolled in {course.course_name}")

        def view_enroll_course(self):

            print(f"\nCourses enrolled by {self.name}:")

            if not self.enrolled_courses:
             print("no courses enrolled")

            for data in self.enrolled_courses.values():
             course = data["course"]
             progress = data["progress"]

             print(
                f"- {course.course_name} | "
                f"Progress: {progress}%"
            )
        


        def check_progress(self,course_id):
             if course_id in self.enrolled_courses:
                  progress = self.enrolled_courses[course_id]["progress"]
                  print(f"{self.name}'s progress: "f"{progress}%")
             else:
                  print("student has not enrolled to this course")


        def update_progress(self,course_id,progress):
             if course_id in self.enrolled_courses:
                  if 0 <= progress <= 100:
                   self.enrolled_courses[course_id]["progress"] = progress
                   print(f"Progress updated to {progress}%")
                  else:
                   print("Progress must be between 0 and 100.")
             else:
                  print("Student is not enrolled in this course.")
             
             