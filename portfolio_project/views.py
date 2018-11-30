from django.shortcuts import render, get_list_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.paginator import Paginator
from .models import Article

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home_view(request):
    return render(request, 'generic/home.html')


def projects_view(request):
    return render(request, 'generic/projects.html')


@cache_page(CACHE_TTL)
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
