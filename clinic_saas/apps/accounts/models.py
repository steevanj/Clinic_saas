from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.clinic.models import Clinic

class User(AbstractUser):
    """
    Custom user tied to a clinic
    """

    ROLE_CHOICES = (
        ("ADMIN", "Clinic Admin"),
        ("RECEPTIONIST", "Receptionist"),
        ("DOCTOR", "Doctor"),
    )

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
