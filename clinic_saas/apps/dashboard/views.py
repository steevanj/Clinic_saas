from django.shortcuts import render
from django.utils.timezone import now
from apps.patients.models import Patient
from apps.doctors.models import Doctor
from apps.appointments.models import Appointment
from apps.billing.models import Invoice

def dashboard_view(request):
    today = now().date()

    context = {
        "patients_count": Patient.objects.count(),
        "doctors_count": Doctor.objects.count(),
        "today_appointments": Appointment.objects.filter(
            appointment_date=today
        ).count(),
        "pending_invoices": Invoice.objects.filter(
            payment_status="PENDING"
        ).count(),
    }

    return render(request, "dashboard/index.html", context)
