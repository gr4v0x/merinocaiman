import hashlib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import MainIdenForm, AddNoteForm
from .models import MainIden

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
    main_idens = MainIden.objects.all()
    return render(request, 'fms/identities.html', {'main_idens': main_idens})

@login_required
def add_iden(request):
    if request.method == "POST":
        main_iden_form = MainIdenForm(request.POST)
        if main_iden_form.is_valid():
            main_iden = main_iden_form.save(commit=False)
            mk = hashlib.sha1()
            mk.update(main_iden.lastName)
            mk.update(main_iden.firstName)
            mk.update(main_iden.otherName)
            mk.update(str(main_iden.dateOfBirth))
            main_iden.mainIdenKey = mk.hexdigest()
            main_iden.save()
            return redirect('identities')
    else:
        main_iden_form = MainIdenForm()
    return render(request, 'fms/add_iden.html', {'form': main_iden_form})

@login_required
def tasks(request):
    return render(request, 'fms/tasks.html', {})

@login_required
def notebook(request):
    return render(request, 'fms/notebook.html', {})

@login_required
def add_note(request):
    add_note_form = AddNoteForm()
    return render(request, 'fms/add_note.html', {'form': add_note_form})
