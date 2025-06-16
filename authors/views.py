from django.shortcuts import render
from .forms import RegisterForm


def register(request):
    form = RegisterForm()
    return render(request, 'authors/pages/register.html', {
        'form': form,
    })
