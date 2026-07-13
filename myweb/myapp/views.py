from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")
