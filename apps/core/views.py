from django.shortcuts import render
from .models import Profile


def home(request):
    profile = (
        Profile.objects
        .prefetch_related(
            "experience",
            "skills",
            "education",
            "certifications",
            "projects__experience",
        )
        .order_by("id")
        .first()
    )

    return render(request, "core/home.html", {"profile": profile})