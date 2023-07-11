from django.shortcuts import render
from django.conf import settings



def home(request):
    return render(request, 'index.html', )

def about(request):
    return render(request, 'about.html', )


def causes(request):
    return render(request, 'causes.html', )


def gallery(request):
    return render(request, 'gallery.html', )


def contact(request):
    return render(request, 'contact.html', )