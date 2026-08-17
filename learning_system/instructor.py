from parent import User
class Instructor(User):
        def __init__(self, name, email, userid):
                super().__init__(name, email, userid)
                self.courses = []



        def create_course(self, course):
           self.courses.append(course)

           print(
            f"{self.name} created course: "
            f"{course.course_name}"
        )

        def display_courses(self):
         print(f"\nCourses taught by {self.name}:")

         if not self.courses:
            print("No courses created.")
            return

         for course in self.courses:
            print(
                f"- {course.course_name} "
                f"(Course ID: {course.course_id})"
            )

            

                

        