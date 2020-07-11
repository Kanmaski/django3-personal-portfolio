from django.shortcuts import render
from .models import Project
from .forms import NameForm, ContactForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    projects = Project.objects.all()
    forms = formset_factory(ContactForm, extra=2)
    formset= forms()
    return render(request, 'portfolio/home.html', {'projects':projects, 'forms': formset})