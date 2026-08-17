"""
Create a basic E-Learning Platform using OOP and inheritance.

Create a parent User class containing common information such as name, email, and user ID.

Create two child classes

Student

Instructor

A student should be able to enroll in a course, view enrolled courses, and check course progress.

An instructor should be able to create courses and display the courses they are teaching.

Create at least 2 students, 2 instructors, and 3 courses and demonstrate how inheritance is being used.

"""
from instructor import Instructor
from course import Course
from student import Student

if __name__ == "__main__":
    student1 = Student("Ramesh","ramesh@gmail.com",123)
    student2 = Student("sumesh","sumesh@gmail.com",321)

    instructor1 = Instructor("sham","sham@gmail.com",987)
    instructor2 = Instructor("sam","sam@gmail.com",456)
    instructor3 = Instructor("sid","sid@gmail.com",852)

    course1 = Course(1245,"Intro to Java");
    course2 = Course(4567,"Intro to python");
    course3 = Course(741,"Intro to AI");

    instructor1.create_course(course1)
    instructor1.create_course(course2)

    instructor2.create_course(course3)

    student1.enroll_course(course1)
    student2.enroll_course(course2)
    student2.enroll_course(course2)

    student1.view_enroll_course()
    student2.view_enroll_course()

    student1.check_progress(123)

    student2.check_progress(321)

    student1.update_progress(123, 60)
    student2.update_progress(321, 40)
    student1.check_progress(123)
    
    student2.check_progress(321)


  

