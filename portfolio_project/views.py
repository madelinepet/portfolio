from django.shortcuts import render


def home_view(request):
    return render(request, 'generic/home.html')


def projects_view(request):
    return render(request, 'generic/projects.html')


def vis_view(request):
    return render(request, 'generic/vis.html')
