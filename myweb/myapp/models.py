from django.db import models
from django.contrib import admin


# Create your models here.
# st_id, fname, lname

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นาง", "นาง"),
    ("นางสาว", "นางสาว"),
)


class Major(models.Model):
    mj_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.mj_name

    def get_absolute_url(self):
        return reversed("Major_detall", kwargs={"pk": self.pk})


class Student(models.Model):
    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default="นาย")
    st_id = models.CharField(max_length=10, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reversed("Student_detall", kwargs={"pk": self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = ["st_id", "prefix_name", "fname", "lname", "major"]


class MajorAdmin(admin.ModelAdmin):
    list_display = ["mj_name"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Major, MajorAdmin)
