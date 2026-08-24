from django.db import models
from django.contrib import admin
from django.urls import reverse


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
        return reverse("major_detail", kwargs={"pk": self.pk})


class Student(models.Model):
    prefix_name = models.CharField(max_length=10, choices=PREFIX_NAME, default="นาย")
    st_id = models.CharField(max_length=10, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="หมวดหมู่วิชา")

    class Meta:
        verbose_name = "หมวดหมู่วิชา"
        verbose_name_plural = "หมวดหมู่วิชา"

    def __str__(self):
        return self.name


class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name="รหัสวิชา")
    title = models.CharField(max_length=200, blank=False, verbose_name="ชื่อวิชา")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subjects",
        verbose_name="หมวดหมู่",
    )

    class Meta:
        verbose_name = "รายวิชา"
        verbose_name_plural = "รายวิชา"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} {self.title}"

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = ["st_id", "prefix_name", "fname", "lname", "major"]


class MajorAdmin(admin.ModelAdmin):
    list_display = ["mj_name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["code", "title", "category"]
    search_fields = ["code", "title"]
    list_filter = ["category"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
