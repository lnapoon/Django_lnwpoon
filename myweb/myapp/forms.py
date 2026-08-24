from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["st_id", "prefix_name", "fname", "lname", "major"]
        labels = {
            "st_id": "รหัสนักศึกษา",
            "prefix_name": "คำนำหน้าชื่อ",
            "fname": "ชื่อ",
            "lname": "นามสกุล",
            "major": "สาขาวิชา",
        }
        widgets = {
            "st_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "กรอกรหัสนักศึกษา (เช่น 6500000001)",
                    "required": True,
                }
            ),
            "prefix_name": forms.Select(attrs={"class": "form-select"}),
            "fname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "กรอกชื่อ",
                    "required": True,
                }
            ),
            "lname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "กรอกนามสกุล",
                    "required": True,
                }
            ),
            "major": forms.Select(attrs={"class": "form-select"}),
        }
