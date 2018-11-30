from django.shortcuts import render
# from .models import Article


def vis_view(request, data=None):
    """ This is the function defining the list view of all articles. Context 
    is sent to the template and can be accessed there
    """

    context = {
        'articles': [
            {
                'title': 'wazzap',
            },
            {
                'description': 'fake description',
            },
            {
                'source': 'fake source',
            },
            {
                'date_published': 'date_published',
            },
            {
                'url': 'url',
            },
            {
                'dom_tone': 'dom_tone',
            },
            {
                'image': 'image',
            },
        ]
    }

    return render(request, 'news/vis.html', context)
