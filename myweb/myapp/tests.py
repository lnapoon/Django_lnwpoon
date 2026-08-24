from django.test import TestCase
from django.urls import reverse
from .models import Student, Major


class StudentCRUDTest(TestCase):
    def setUp(self):
        self.major = Major.objects.create(mj_name="วิทยากรรมคอมพิวเตอร์")
        self.student = Student.objects.create(
            st_id="65010001",
            prefix_name="นาย",
            fname="สมชาย",
            lname="ใจดี",
            major=self.major,
        )

    def test_student_list(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "65010001")
        self.assertContains(response, "สมชาย")

    def test_student_detail(self):
        response = self.client.get(reverse("student_detail", kwargs={"pk": self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "65010001")
        self.assertContains(response, "สมชาย")

    def test_student_create(self):
        response = self.client.post(
            reverse("student_create"),
            {
                "st_id": "65010002",
                "prefix_name": "นางสาว",
                "fname": "สมหญิง",
                "lname": "รักดี",
                "major": self.major.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(st_id="65010002").exists())

    def test_student_edit(self):
        response = self.client.post(
            reverse("student_edit", kwargs={"pk": self.student.pk}),
            {
                "st_id": "65010001",
                "prefix_name": "นาย",
                "fname": "สมชาย",
                "lname": "เก่งกาจ",
                "major": self.major.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.lname, "เก่งกาจ")

    def test_student_delete(self):
        response = self.client.post(
            reverse("student_delete", kwargs={"pk": self.student.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
