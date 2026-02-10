from django.db import models
from django.core.validators import MinValueValidator
from apps.patients.models import Patient
from apps.doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = (
        ("SCHEDULED", "Scheduled"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
        ("NO_SHOW", "No Show"),
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name="appointments"
    )

    appointment_date = models.DateField(help_text="Date of appointment")
    appointment_time = models.TimeField(help_text="Start Time of appointment")

    expected_duration_minutes = models.PositiveIntegerField(
        default=15,
        validators=[MinValueValidator(5)],
        help_text="Expected consultation duration"
    )

    status = models.CharField(
        max_length=20,
        default="SCHEDULED",
        choices=STATUS_CHOICES,
        db_index=True
    )

    reason_for_visit = models.TextField(
        max_length=255,
        help_text="Chief Complaints / Reason for visit"
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Internal Notes by staff or doctor"
    )

    cancelled_reason = models.TextField(
        max_length=255,
        null=True,
        blank=True
    )

    checked_in_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When patient arrived"
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Fee charged for this appointment"
    )

    is_billed = models.BooleanField(
        default=False,
        help_text="Has invoice been generated"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time']
        indexes = [
            models.Index(fields=['appointment_date', 'doctor']),
            models.Index(fields=['status']),
        ]
        unique_together = (
            "doctor",
            "appointment_date",
            "appointment_time",
        )

    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.user.get_full_name()}"

    @property
    def end_time(self):
        from datetime import datetime, timedelta
        start = datetime.combine(self.appointment_date, self.appointment_time)
        return (start + timedelta(minutes=self.expected_duration_minutes)).time()
