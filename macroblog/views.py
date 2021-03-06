from django.shortcuts import render

from random import choice

from blog.models import Post
from widgets.models import Quote, Bookmark


def IndexView(request):
    recent_posts = Post.public_post.filter(status__gte=2).order_by('-publish')[:2]
    post_count = Post.public_post.filter(status__gte=2).count()
    bookmarks = Bookmark.objects.filter(status__gte=2)[:2]
    bookmark_count = len(Bookmark.objects.filter(status__gte=2))
    all_quotation = Quote.objects.filter(use_it='True').values_list('quotation','quoted_by')

    if len(all_quotation) > 0:
        quotation, author = choice(all_quotation)
    else:
        quotation = "If I had eight hours to chop down a tree, I'd spend the first six of them sharpening my axe."
        author = "Abraham Lincoln"

    return render(request, 'index.html', {'quotation': quotation, 'author': author,
        'recent_posts': recent_posts, 'post_count': post_count, 'bookmarks': bookmarks,
        'bookmark_count': bookmark_count, })

