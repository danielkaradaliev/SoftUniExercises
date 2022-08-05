from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    NAME = "Dimcho"
    NOTES = ["something noted", "something else noted", "etc."]

    def test__init__do_not_pass_courses__expect_not_to_be_enrolled_in_any_courses(self):
        self.test_student = Student(self.NAME)
        self.assertEqual(self.test_student.name, self.NAME)
        self.assertEqual(self.test_student.courses, dict())

    def test__init__pass_courses__expect_to_have_them(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)
        self.assertEqual(new_student.name, self.NAME)
        self.assertEqual(new_student.courses, dummy_courses)

    def test__enroll__pass_notes_for_existing_course_with_no_optional_parameter__expect_to_update_notes(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)
        expected_notes = [x for x in new_student.courses["Javascript"]] + self.NOTES
        actual_result = new_student.enroll("Javascript", self.NOTES)
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], expected_notes)

    def test__enroll__pass_new_course_with_correct_optional_parameter__expect_to_add_course_with_passed_notes(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        actual_result = new_student.enroll("C++", self.NOTES, "Y")
        expected_result = "Course and course notes have been added."
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(new_student.courses["C++"], self.NOTES)
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])

    def test__enroll__pass_new_course_without_optional_parameter__expect_to_add_course_with_passed_notes(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        actual_result = new_student.enroll("C", self.NOTES)
        expected_result = "Course and course notes have been added."
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(new_student.courses["C"], self.NOTES)
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])

    def test__enroll__pass_new_course_with_notes_and_with_bad_optional_parameter__expect_to_have_a_new_course_without_notes(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        actual_result = new_student.enroll("Bash", self.NOTES, "brrrt")
        expected_result = "Course has been added."
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(new_student.courses["Bash"], list())
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])

    def test__enroll__pass_new_course_with_no_notes_and_with_bad_optional_parameter__expect_to_have_a_new_course_without_notes(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        actual_result = new_student.enroll("Pascal", list(), "turlu_giuvech")
        expected_result = "Course has been added."
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(new_student.courses["Pascal"], list())
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])

    def test__add_notes__pass_existing_course__expect_to_append_note(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        note_to_add = "amazing"
        expected_notes = [x for x in dummy_courses["Python"]] + [note_to_add]
        actual_result = new_student.add_notes("Python", note_to_add)
        expected_result = "Notes have been updated"
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(new_student.courses["Python"], expected_notes)
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])

    def test__add_notes__pass_invalid_course__expect_to_raise(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        note_to_add = "what language is this for again?"
        non_existing_course = "Typescript"
        expected_result = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ex:
            new_student.add_notes(non_existing_course, note_to_add)
        self.assertEqual(str(ex.exception), expected_result)
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])

    def test__leave_course__pass_valid_course__expect_not_to_be_in_courses_anymore(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        course_to_remove = "Javascript"
        actual_result = new_student.leave_course(course_to_remove)
        expected_result = "Course has been removed"
        self.assertEqual(actual_result, expected_result)
        self.assertTrue(course_to_remove not in new_student.courses.keys())
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])

    def test__leave_course__pass_invalid_course__expect_to_raise(self):
        dummy_courses = {
            "Python": ["Cool language", "hissssss..."],
            "Javascript": ["Please no", "leave me alone", "why do you exist?", "one framework too many?"]
        }
        new_student = Student(self.NAME, dummy_courses)

        course_to_remove = "MySQL"
        expected_result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ex:
            new_student.leave_course(course_to_remove)
        self.assertEqual(str(ex.exception), expected_result)
        self.assertEqual(new_student.courses["Python"], dummy_courses["Python"])
        self.assertEqual(new_student.courses["Javascript"], dummy_courses["Javascript"])


if __name__ == "__main__":
    main()
