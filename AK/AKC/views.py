from django.shortcuts import render,redirect,HttpResponse
from django.templatetags.static import static
# Create your views here.

def home(request):
    slides = [
        static("banner1.png"),
        static("banner2.png"),
        static("banner3.jpg"),
    ]
    return render(request, "index.html", {"slides": slides})