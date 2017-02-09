from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import MainIdenForm

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'fms/dashboard.html', {})

@login_required
def documents(request):
    return render(request, 'fms/documents.html', {})

@login_required
def docs_for_disclosure(request):
    return render(request, 'fms/docs_for_disclosure.html', {})

@login_required
def docs_not_disclosure(request):
    return render(request, 'fms/docs_not_disclosure.html', {})

@login_required
def docs_exhibits(request):
    return render(request, 'fms/exhibits.html', {})

@login_required
def main_identities(request):
    return render(request, 'fms/identities.html', {})

@login_required
def add_iden(request):
    main_iden_form = MainIdenForm()
    return render(request, 'fms/add_iden.html', {'form': main_iden_form})

@login_required
def tasks(request):
    return render(request, 'fms/tasks.html', {})

@login_required
def notebook(request):
    return render(request, 'fms/notebook.html', {})
