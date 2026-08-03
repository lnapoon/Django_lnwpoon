from django.db import models
from django.contrib import admin


# Create your models here.
# st_id, fname, lname

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นาง", "นาง"),
    ("นางสาว", "นางสาว"),
)


class Student(models.Model):
    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default="นาย")
    st_id = models.CharField(max_length=10, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reversed("Student_detall", kwargs={"pk": self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = ["st_id", "prefix_name", "fname", "lname"]


admin.site.register(Student, StudentAdmin)
