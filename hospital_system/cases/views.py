from django.shortcuts import render, redirect, get_object_or_404
from .models import Case, Patient
from .forms import CaseForm, PatientForm


# ---------------------------CASE---------------------------
def case_list_view(request):
    obj = Case.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'case/case_list.html', context)


def case_create_view(request):
    form = CaseForm()
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            Case.objects.create(**form.cleaned_data)
            form = CaseForm()
            return redirect('../list')

    context = {
        'form': form
    }
    return render(request, 'case/case_create.html', context)


def case_update_view(request, id):
    obj = get_object_or_404(Case, id=id)
    context = {}
    form = CaseForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/case/list')
    context['form'] = form

    return render(request, 'case/case_update.html', context)


def case_index_view(request, id):
    obj = Case.objects.get(id=id)
    context = {
        'obj': obj
    }
    return render(request, 'case/case_index.html', context)


def case_delete_view(request, id):
    obj = get_object_or_404(Case, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../list')

    context = {
        'obj': obj
    }
    return render(request, 'case/case_delete.html', context)


# ---------------------------PATIENT---------------------------
def patient_list_view(request):
    obj = Patient.objects.all()
    context = {
        'obj': obj
    }

    return render(request, 'patient/patient_list.html', context)


def patient_create_view(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            Patient.objects.create(**form.cleaned_data)
            return redirect('/case/list')

    context = {
        'form': form
    }
    return render(request, 'patient/patient_create.html', context)


def patient_index_view(request, id):
    obj = Patient.objects.get(id=id)
    context = {
        'obj': obj
    }

    return render(request, 'patient/patient_index.html', context)


def patient_delete_view(request, id):
    obj = Patient.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/case/patient/list')

    context = {
        'obj': obj
    }

    return render(request, 'patient/patient_delete.html', context)


def patient_update_view(request, id):
    context = {}
    obj = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/case/patient/list')

    context["form"] = form
    return render(request, 'patient/patient_update.html', context)
