from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#vista basada en funciones
@login_required()

def show_index(request):
    return render(request, 'index.html')

#vista basada en clases

class ShowIndex(TemplateView):
    template_name ='index.html'