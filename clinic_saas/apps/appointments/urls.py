from django.urls import path
from . import views

app_name = "appointments"

urlpatterns = [
    path("", views.appointment_list, name="list"),
    path("status/<int:pk>/", views.update_status, name="update_status"),
]
