from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'mrn', 'name', 'gender', 'age', 'phone',
        'email', 'blood_group', 'insurance_provider',
        'created_at', 'updated_at'
    ]
    search_fields = ['mrn', 'name', 'phone', 'email']
    list_filter = ['gender', 'blood_group', 'insurance_provider', 'created_at']
    ordering = ['name']
    def age(self, obj):
        return obj.age
    age.short_description = 'Age'
