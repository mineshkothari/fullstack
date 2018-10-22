from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


# Create your views here.
def index(request):
    latest_post = Post.objects.filter(published_date__lte=timezone.now()
                                      ).order_by('-published_date').first()

    return render(request, 'home/index.html', {'post': latest_post})
