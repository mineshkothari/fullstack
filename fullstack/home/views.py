from django.shortcuts import render, redirect
from blog.models import Post
from courses.models import Language
from django.utils import timezone


# Create your views here.
def index(request):
    latest_post = Post.objects.filter(published_date__lte=timezone.now()
                                      ).order_by('-published_date').first()

    languages = Language.objects.all().order_by('id')

    args = {
        'post': latest_post,
        'languages': languages,
    }

    return render(request, 'home/index.html', args)


def my_custom_page_not_found_view(request):
    return redirect('index')
