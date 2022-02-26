from django.shortcuts import render

# Create your views here.
def home(request):
    info = "Sean"
    return render(request, "index.html", {"info": info})