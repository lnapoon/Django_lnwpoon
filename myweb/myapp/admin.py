from django.contrib import admin
from .models import Student, Major, Category, Subject


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
