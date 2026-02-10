from django.db import models

class Clinic(models.Model):
    """
    Represents one clinic (tenant)
    """

    name = models.CharField(max_length=150)
    registration_number = models.CharField(
        max_length=100,
        unique=True,
        help_text="Clinic registration / license number"
    )

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    address = models.TextField()

    # Branding (future SaaS)
    logo = models.ImageField(
        upload_to="clinic_logos/",
        null=True,
        blank=True
    )

    # Status
    is_active = models.BooleanField(default=True)

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Clinic"
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.name
