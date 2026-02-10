from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Doctor
from django.contrib.auth.decorators import login_required


User = get_user_model()   # 👈 THIS WAS MISSING

@login_required
def doctor_list(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST["email"],
            email=request.POST["email"],
            password="doctor@123",
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            role="DOCTOR",                 # 👈 REQUIRED
            clinic=request.user.clinic     # 👈 REQUIRED
        )

        Doctor.objects.create(
            user=user,
            registration_number=request.POST["registration_number"],
            specialization=request.POST["specialization"],
            qualification=request.POST["qualification"],
            experience_years=request.POST["experience_years"],
            consultation_fee=request.POST["consultation_fee"],
            available_from=request.POST["available_from"],
            available_to=request.POST["available_to"],
            phone=request.POST["phone"],
        )

        return redirect("doctors:list")

    doctors = Doctor.objects.select_related("user")

    return render(request, "doctors/list.html", {
        "doctors": doctors
    })
