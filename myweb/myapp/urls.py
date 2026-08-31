from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Auth routes
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    # Student CRUD
    path("student/create/", views.student_create, name="student_create"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("student/<int:pk>/edit/", views.student_edit, name="student_edit"),
    path("student/<int:pk>/delete/", views.student_delete, name="student_delete"),

    # Subject CRUD
    path("subjects/", views.subject_list, name="subject_list"),
    path("subjects/create/", views.subject_create, name="subject_create"),
    path("subjects/<int:pk>/", views.subject_detail, name="subject_detail"),
    path("subjects/<int:pk>/edit/", views.subject_edit, name="subject_edit"),
    path("subjects/<int:pk>/delete/", views.subject_delete, name="subject_delete"),
]
