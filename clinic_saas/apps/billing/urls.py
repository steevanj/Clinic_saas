from django.urls import path
from . import views

app_name = "billing"

urlpatterns = [
    path("", views.billing_list, name="list"),
    path("generate/<int:appointment_id>/", views.generate_invoice, name="generate"),
    path("pay/<int:invoice_id>/", views.mark_invoice_paid, name="pay"),
]
