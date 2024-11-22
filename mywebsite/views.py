from django.shortcuts import render

def index_view(request):
    return render(request, 'mywebsite/index.html')

def about_view(request):
    return render(request, 'mywebsite/about.html')

def resume_view(request):
    return render(request, 'mywebsite/resume.html')

def contact_view(request):
    return render(request, 'mywebsite/contact.html')

