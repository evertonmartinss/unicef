from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *

def country_view(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/country')

    else:
        form = CountryForm()

    return render(request, 'template/form.html', {'form': form})


def dieta_view(request):
    if request.method == 'POST':
        form = MortalityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mortality')

    else:
        form = MortalityForm()

    return render(request, 'template/form.html', {'form': form})