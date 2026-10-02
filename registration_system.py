class StudentCourseRegistrationSystem:
    def __init__(self):
        self.users = {"S101": "Pass123"}
        self.logged_in_users = set()
        self.courses = {
            "CS101": {"capacity": 30, "enrolled": ["S102"]},
            "CS102": {"capacity": 1, "enrolled": ["S103"]}  # Full course
        }

    def login(self, student_id, password):
        if self.users.get(student_id) == password:
            self.logged_in_users.add(student_id)
            return True, "Login successful"
        return False, "Invalid credentials"

    def register_course(self, student_id, course_id):
        if student_id not in self.logged_in_users:
            return False, "User not logged in"
        
        course = self.courses.get(course_id)
        if not course:
            return False, "Course does not exist"
        
        if student_id in course["enrolled"]:
            return False, "Already registered for this course"
        
        if len(course["enrolled"]) >= course["capacity"]:
            return False, "Course is full"
        
        course["enrolled"].append(student_id)
        return True, "Registration successful"

    def drop_course(self, student_id, course_id):
        if student_id not in self.logged_in_users:
            return False, "User not logged in"
        
        course = self.courses.get(course_id)
        if not course or student_id not in course["enrolled"]:
            return False, "Course not registered"
        
        course["enrolled"].remove(student_id)
        return True, "Course dropped successfully"