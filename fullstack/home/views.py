from django.shortcuts import render
from blog.models import Post
from courses.models import Language
from django.utils import timezone


# Create your views here.
def index(request):
    latest_post = Post.objects.filter(published_date__lte=timezone.now()
                                      ).order_by('-published_date').first()

    languages = Language.objects.all()

    args = {
        'post': latest_post,
        'languages': languages,
    }

    return render(request, 'home/index.html', args)
