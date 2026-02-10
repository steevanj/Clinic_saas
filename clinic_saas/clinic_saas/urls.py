from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.dashboard.urls")),
    path('accounts/', include('apps.accounts.urls')),
    path('appointments/', include('apps.appointments.urls')),
    path('billing/', include('apps.billing.urls')),
    path('clinic/', include('apps.clinic.urls')),
    path('doctors/', include('apps.doctors.urls')),
    path('patients/', include('apps.patients.urls')),
]
