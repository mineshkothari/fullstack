from django.shortcuts import render


def about(request):
    """
    Render about page
    """
    return render(request, 'about/about.html')
