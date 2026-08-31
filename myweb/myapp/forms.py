from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Student, Subject, Category


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


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["sub_code", "sub_name"]
        labels = {
            "sub_code": "รหัสวิชา",
            "sub_name": "ชื่อรายวิชา",
        }
        widgets = {
            "sub_code": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกรหัสวิชา (เช่น CS101)",
                    "aria-label": "รหัสวิชา",
                    "required": True,
                }
            ),
            "sub_name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "กรอกชื่อรายวิชา (เช่น พื้นฐานวิทยาการคอมพิวเตอร์)",
                    "aria-label": "ชื่อรายวิชา",
                    "required": True,
                }
            ),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="ชื่อผู้ใช้ (Username)",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "กรอกชื่อผู้ใช้",
                "aria-label": "ชื่อผู้ใช้",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        label="รหัสผ่าน (Password)",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "กรอกรหัสผ่าน",
                "aria-label": "รหัสผ่าน",
            }
        ),
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        labels = {
            "username": "ชื่อผู้ใช้ (Username)",
            "email": "อีเมล (Email)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "ตั้งชื่อผู้ใช้สำหรับเข้าสู่ระบบ",
                "aria-label": "ชื่อผู้ใช้",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "กรอกอีเมลของคุณ (เช่น user@example.com)",
                "aria-label": "อีเมล",
            }
        )
        if "password1" in self.fields:
            self.fields["password1"].widget.attrs.update(
                {
                    "class": "form-control form-control-lg",
                    "placeholder": "ตั้งรหัสผ่าน",
                    "aria-label": "รหัสผ่าน",
                }
            )
        if "password2" in self.fields:
            self.fields["password2"].widget.attrs.update(
                {
                    "class": "form-control form-control-lg",
                    "placeholder": "ยืนยันรหัสผ่านอีกครั้ง",
                    "aria-label": "ยืนยันรหัสผ่าน",
                }
            )
