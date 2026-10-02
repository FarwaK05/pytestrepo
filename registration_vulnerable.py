import sqlite3

class VulnerableRegistrationSystem:
    def __init__(self):
        # Vulnerability 1: Hardcoded credentials
        self.db_password = "SuperSecretPassword123!"

    def login_student(self, student_id, password):
        conn = sqlite3.connect("registration.db")
        cursor = conn.cursor()
        
        # Vulnerability 2: SQL Injection flaw
        query = f"SELECT * FROM students WHERE id = '{student_id}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        
        # Vulnerability 3: Plaintext logging of sensitive user credentials
        print(f"DEBUG LOG: User {student_id} attempt with password: {password}")
        
        return user