from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm
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

    if request.method == "POST":
        if not profile:
            messages.error(request, "Portfolio is not configured yet.")
            return redirect("core:home")

        form = ContactForm(request.POST)
        if form.is_valid():
            message_obj = form.save(commit=False)
            message_obj.profile = profile
            message_obj.save()

            recipient_list = [profile.email]
            owner_email = getattr(settings, "PORTFOLIO_CONTACT_EMAIL", "")
            if owner_email and owner_email not in recipient_list:
                recipient_list.append(owner_email)

            send_mail(
                subject=f"[Portfolio] {message_obj.subject}",
                message=(
                    f"From: {message_obj.name} <{message_obj.email}>\n\n"
                    f"{message_obj.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_list,
                fail_silently=False,
            )

            messages.success(request, "Thanks. Your message has been sent.")
            return redirect("core:home")

        messages.error(request, "Please fix the errors below.")
    else:
        form = ContactForm()

    return render(
        request,
        "core/home.html",
        {
            "profile": profile,
            "contact_form": form,
        },
    )