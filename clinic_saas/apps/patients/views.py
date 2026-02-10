from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
from .models import Patient

def generate_mrn():
    from .models import Patient
    while True:
        mrn = 'MRN-' + get_random_string(8).upper()
        if not Patient.objects.filter(mrn=mrn).exists():
            return mrn

def patient_list(request):
    if request.method == 'POST':
        Patient.objects.create(
            mrn = generate_mrn(),
            name = request.POST.get('name'),
            date_of_birth = request.POST.get('date_of_birth') or None,
            gender = request.POST.get('gender'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email') or None,
            address = request.POST.get('address'),
            blood_group = request.POST.get('blood_group') or None,
            insurance_provider = request.POST.get('insurance_provider'),
            insurance_number = request.POST.get('insurance_number'),
            emergency_contact_name = request.POST.get('emergency_contact_name'),
            emergency_contact_phone = request.POST.get('request_contact_phone'),
            medical_history = request.POST.get('medical_history'),
        )
        return redirect('patients:list')
    patients = Patient.objects.all()
    return render(request,'patients/list.html',{'patients' : patients})
