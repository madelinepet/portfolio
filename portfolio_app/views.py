from django.shortcuts import render
# from .models import Article


def vis_view(request):
    """ This is the function defining the list view of all articles in a
    paginated way with 10 items per page.
    """
    return render(request, 'news/vis.html')
