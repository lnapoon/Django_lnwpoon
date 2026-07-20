from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    import datetime
    
    context = {
        "title": "My Home page",
        
    }
    context["date"] = datetime.date.today()
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
