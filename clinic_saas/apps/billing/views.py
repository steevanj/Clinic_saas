from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Invoice
from apps.appointments.models import Appointment

def billing_list(request):
    invoices = Invoice.objects.select_related(
        "appointment__patient",
        "appointment__doctor__user"
    )

    return render(request, "billing/list.html", {
        "invoices": invoices
    })


def generate_invoice(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        status="COMPLETED"
    )

    if hasattr(appointment, "invoice"):
        return redirect("billing:list")

    subtotal = appointment.consultation_fee
    tax = subtotal * 0.05  # 5% GST example
    total = subtotal + tax

    Invoice.objects.create(
        appointment=appointment,
        subtotal=subtotal,
        tax_amount=tax,
        total_amount=total
    )

    appointment.is_billed = True
    appointment.save()

    return redirect("billing:list")


def mark_invoice_paid(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    if request.method == "POST":
        invoice.mark_paid(
            method=request.POST["payment_method"],
            reference=request.POST.get("transaction_reference")
        )

    return redirect("billing:list")
