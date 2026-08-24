import datetime
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Student
from .forms import StudentForm


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


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        "title": f"ข้อมูลนักศึกษา: {student.fname} {student.lname}",
        "student": student,
    }
    return render(request, "student_detail.html", context)


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
