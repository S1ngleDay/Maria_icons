from django.shortcuts import render


def contact(request):
    return render(request, '../templates/contact/contact.html')
