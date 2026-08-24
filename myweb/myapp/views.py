from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import Student, Subject, Category
from .forms import StudentForm, SubjectForm


def is_admin_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


# Create your views here.
def index(request):
    context = {
        "title": "รายชื่อนักศึกษาทั้งหมด",
        "students": Student.objects.all().order_by("st_id"),
        "date": datetime.date.today(),
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# ==========================================
# Student CRUD Views
# ==========================================
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        "title": f"ข้อมูลนักศึกษา: {student.fname} {student.lname}",
        "student": student,
    }
    return render(request, "student_detail.html", context)


@user_passes_test(is_admin_user, login_url="/admin/login/")
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm()

    context = {
        "title": "เพิ่มข้อมูลนักศึกษา",
        "form": form,
        "is_edit": False,
    }
    return render(request, "student_form.html", context)


@user_passes_test(is_admin_user, login_url="/admin/login/")
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm(instance=student)

    context = {
        "title": f"แก้ไขข้อมูลนักศึกษา: {student.fname} {student.lname}",
        "form": form,
        "student": student,
        "is_edit": True,
    }
    return render(request, "student_form.html", context)


@user_passes_test(is_admin_user, login_url="/admin/login/")
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("home")

    context = {
        "title": f"ยืนยันการลบข้อมูลนักศึกษา: {student.fname} {student.lname}",
        "student": student,
    }
    return render(request, "student_confirm_delete.html", context)


# ==========================================
# Subject CRUD Views
# ==========================================
def subject_list(request):
    category_id = request.GET.get("category")
    if category_id:
        subjects = Subject.objects.filter(category_id=category_id).select_related(
            "category"
        )
    else:
        subjects = Subject.objects.all().select_related("category")

    categories = Category.objects.all()

    context = {
        "title": "รายวิชาเรียนทั้งหมด",
        "subjects": subjects,
        "categories": categories,
        "selected_category": (
            int(category_id) if category_id and category_id.isdigit() else None
        ),
        "date": datetime.date.today(),
    }
    return render(request, "subject_list.html", context)


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    context = {
        "title": f"ข้อมูลรายวิชา: {subject.code} {subject.title}",
        "subject": subject,
    }
    return render(request, "subject_detail.html", context)


@user_passes_test(is_admin_user, login_url="/admin/login/")
def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save()
            return redirect("subject_detail", pk=subject.pk)
    else:
        form = SubjectForm()

    context = {
        "title": "เพิ่มข้อมูลรายวิชา",
        "form": form,
        "is_edit": False,
    }
    return render(request, "subject_form.html", context)


@user_passes_test(is_admin_user, login_url="/admin/login/")
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            subject = form.save()
            return redirect("subject_detail", pk=subject.pk)
    else:
        form = SubjectForm(instance=subject)

    context = {
        "title": f"แก้ไขข้อมูลรายวิชา: {subject.code} {subject.title}",
        "form": form,
        "subject": subject,
        "is_edit": True,
    }
    return render(request, "subject_form.html", context)


@user_passes_test(is_admin_user, login_url="/admin/login/")
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject.delete()
        return redirect("subject_list")

    context = {
        "title": f"ยืนยันการลบรายวิชา: {subject.code} {subject.title}",
        "subject": subject,
    }
    return render(request, "subject_confirm_delete.html", context)
