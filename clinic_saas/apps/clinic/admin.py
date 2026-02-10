from django.contrib import admin
from .models import Clinic


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "registration_number",
        "email",
        "phone",
        "created_at",
    )
    search_fields = ("name", "registration_number", "email")
    list_filter = ("created_at",)
