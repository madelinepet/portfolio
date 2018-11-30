from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Article


def vis_view(request):
    """ This is the function defining the list view of all articles in a
    paginated way with 10 items per page.
    """
    vis_query = get_list_or_404(Article)

    paginator = Paginator(vis_query, 10)

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles': articles
    }
    return render(request, 'generic/vis_view.html', context)
