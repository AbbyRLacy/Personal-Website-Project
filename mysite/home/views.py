from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

# Create your views here.


def index(request):
    template_name = 'home/index.html'
    return render(request, 'home/index.html')


def elements(request):
    template_name = 'home/elements.html'
    return render(request, 'home/elements.html')


def generic(request):
    template_name = 'home/generic.html'
    return render(request, 'home/generic.html')


# Create your views here.
