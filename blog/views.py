from django.shortcuts import render


def blog_list(request):
    return render(request, '../templates/blog/blog_list.html')
