import pytest

from registration_system import StudentCourseRegistrationSystem


@pytest.fixture
def registration_system():
	return StudentCourseRegistrationSystem()


def test_successful_login(registration_system):
	result = registration_system.login("S101", "Pass123")

	assert result == (True, "Login successful")
	assert "S101" in registration_system.logged_in_users


def test_login_with_invalid_password(registration_system):
	result = registration_system.login("S101", "wrong-password")

	assert result == (False, "Invalid credentials")
	assert "S101" not in registration_system.logged_in_users


def test_registration_without_login_is_rejected(registration_system):
	result = registration_system.register_course("S101", "CS101")

	assert result == (False, "User not logged in")
	assert "S101" not in registration_system.courses["CS101"]["enrolled"]


def test_successful_course_registration(registration_system):
	registration_system.login("S101", "Pass123")

	result = registration_system.register_course("S101", "CS101")

	assert result == (True, "Registration successful")
	assert "S101" in registration_system.courses["CS101"]["enrolled"]


def test_registration_for_full_course_is_rejected(registration_system):
	registration_system.login("S101", "Pass123")

	result = registration_system.register_course("S101", "CS102")

	assert result == (False, "Course is full")
	assert "S101" not in registration_system.courses["CS102"]["enrolled"]


def test_duplicate_registration_is_rejected(registration_system):
	registration_system.login("S101", "Pass123")
	registration_system.register_course("S101", "CS101")

	result = registration_system.register_course("S101", "CS101")

	assert result == (False, "Already registered for this course")
	assert registration_system.courses["CS101"]["enrolled"].count("S101") == 1


def test_successful_course_drop(registration_system):
	registration_system.login("S101", "Pass123")
	registration_system.register_course("S101", "CS101")

	result = registration_system.drop_course("S101", "CS101")

	assert result == (True, "Course dropped successfully")
	assert "S101" not in registration_system.courses["CS101"]["enrolled"]


def test_dropping_unenrolled_course_is_rejected(registration_system):
	registration_system.login("S101", "Pass123")

	result = registration_system.drop_course("S101", "CS101")

	assert result == (False, "Course not registered")
	assert registration_system.courses["CS101"]["enrolled"] == ["S102"]
