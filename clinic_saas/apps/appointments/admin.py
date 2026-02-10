from django.contrib import admin
from .models import Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status',
        'consultation_fee',
        'is_billed',
    ]

    list_filter = ('status','appointment_date','doctor')
    search_fields = (
        'patient_name',
        'doctor_user_username',
        'reason_for_visit',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'checked_in_at',
        'completed_at',
    )