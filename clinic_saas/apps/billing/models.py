from django.db import models
from django.utils import timezone
from apps.appointments.models import Appointment

class Invoice(models.Model):
    PAYMENT_STATUS = (
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("CANCELLED", "Cancelled"),
    )

    PAYMENT_METHOD = (
        ("CASH", "Cash"),
        ("UPI", "UPI"),
        ("CARD", "Card"),
        ("BANK", "Bank Transfer"),
    )

    # 🔗 Core relationship
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="invoice"
    )

    # 💰 Financials
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    tax_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # 💳 Payment tracking
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="PENDING",
        db_index=True
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD,
        null=True,
        blank=True
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    transaction_reference = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # 🧾 Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_paid(self, method, reference=None):
        self.payment_status = "PAID"
        self.payment_method = method
        self.transaction_reference = reference
        self.paid_at = timezone.now()
        self.save()

    def __str__(self):
        return f"Invoice #{self.id} - {self.appointment.patient.name}"
