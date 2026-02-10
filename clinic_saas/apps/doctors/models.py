from django.db import models
from django.conf import settings

class Doctor(models.Model):
    """
    Represents a medical practitioner in the clinic
    """

    # 🔗 Auth
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="doctor_profile"
    )

    # 🩺 Professional details
    registration_number = models.CharField(
        max_length=50,
        unique=True,
        help_text="Medical council registration number"
    )

    specialization = models.CharField(
        max_length=100,
        help_text="Primary specialization"
    )

    qualification = models.CharField(
        max_length=150,
        help_text="Degrees & certifications"
    )

    experience_years = models.PositiveIntegerField(
        default=0
    )

    # 💰 Consultation
    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    # 🕒 Availability
    available_from = models.TimeField()
    available_to = models.TimeField()

    consultation_duration_minutes = models.PositiveIntegerField(
        default=15
    )

    # 📞 Contact
    phone = models.CharField(
        max_length=20,
        unique=True
    )

    # 🟢 Status
    is_active = models.BooleanField(
        default=True,
        help_text="Inactive doctors cannot receive appointments"
    )

    # 🧾 Audit
    joined_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["specialization", "user__first_name"]

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} ({self.specialization})"
