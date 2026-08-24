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
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกรหัสนักศึกษา (เช่น 6500000001)",
                    "aria-label": "รหัสนักศึกษา",
                    "required": True,
                }
            ),
            "prefix_name": forms.Select(
                attrs={
                    "class": "form-select form-select-lg",
                    "aria-label": "คำนำหน้าชื่อ",
                }
            ),
            "fname": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกชื่อ",
                    "aria-label": "ชื่อ",
                    "required": True,
                }
            ),
            "lname": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกนามสกุล",
                    "aria-label": "นามสกุล",
                    "required": True,
                }
            ),
            "major": forms.Select(
                attrs={
                    "class": "form-select form-select-lg",
                    "aria-label": "สาขาวิชา",
                }
            ),
        }
