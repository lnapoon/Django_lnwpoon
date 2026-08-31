from django.contrib import admin
from .models import Student, Major, Category, Subject, Enrolls


class StudentAdmin(admin.ModelAdmin):
    list_display = ["st_id", "prefix_name", "fname", "lname", "major"]


class MajorAdmin(admin.ModelAdmin):
    list_display = ["mj_name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["sub_code", "sub_name"]
    search_fields = ["sub_code", "sub_name"]


class EnrollsAdmin(admin.ModelAdmin):
    list_display = ["student", "subject"]
    list_filter = ["subject"]
    search_fields = [
        "student__fname",
        "student__lname",
        "student__st_id",
        "subject__sub_code",
        "subject__sub_name",
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Enrolls, EnrollsAdmin)
