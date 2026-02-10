from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseBadRequest
from datetime import date
from .models import Appointment
from apps.patients.models import Patient
from apps.doctors.models import Doctor
from django.core.exceptions import ValidationError

def appointment_list(request):
    if request.method == "POST":
        try:
            patient_id = request.POST.get("patient")
            doctor_id = request.POST.get("doctor")

            if not patient_id or not doctor_id:
                return HttpResponseBadRequest("Patient and Doctor are required.")

            patient = get_object_or_404(Patient, pk=patient_id)
            doctor = get_object_or_404(Doctor, pk=doctor_id)

            appointment = Appointment(
                patient=patient,
                doctor=doctor,
                appointment_date=request.POST.get("appointment_date"),
                appointment_time=request.POST.get("appointment_time"),
                expected_duration_minutes=request.POST.get("duration", 15),
                reason_for_visit=request.POST.get("reason", ""),
                consultation_fee=request.POST.get("fee", 0),
                notes=request.POST.get("notes", ""),
            )

            appointment.full_clean()  # model-level validation
            appointment.save()

            return redirect("appointments:list")

        except ValidationError as e:
            return HttpResponseBadRequest(f"Validation error: {e}")
        except Exception as e:
            return HttpResponseBadRequest(f"Error creating appointment: {e}")

    appointments = Appointment.objects.select_related("patient", "doctor__user")

    return render(request, "appointments/list.html", {
        "appointments": appointments,
        "patients": Patient.objects.all(),
        "doctors": Doctor.objects.all(),
        "today": date.today(),
    })


def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, "appointments/detail.html", {"appointment": appointment})


def update_status(request, pk):
    try:
        appointment = get_object_or_404(Appointment, pk=pk)
        status = request.POST.get("status")

        if not status:
            return HttpResponseBadRequest("Status is required.")

        if status == "IN_PROGRESS":
            appointment.checked_in_at = timezone.now()
        elif status == "COMPLETED":
            appointment.completed_at = timezone.now()
        elif status == "CANCELLED":
            appointment.cancelled_at = timezone.now()
            appointment.cancelled_reason = request.POST.get("cancel_reason", "")

        appointment.status = status
        appointment.full_clean()  # enforce model rules
        appointment.save()

        return redirect("appointments:list")

    except ValidationError as e:
        return HttpResponseBadRequest(f"Validation error: {e}")
    except Exception as e:
        return HttpResponseBadRequest(f"Error updating status: {e}")
