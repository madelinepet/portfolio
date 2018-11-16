from django.shortcuts import render


def home_view(request):
    return render(request, 'generic/home.html')


def resume_view(request):
    return render(request, 'generic/resume.html')
