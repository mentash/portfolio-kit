from django.contrib import admin

from .models import (
    Certification,
    ContactMessage,
    Education,
    Experience,
    Profile,
    Project,
    Skill,
)


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    inlines = [EducationInline, ExperienceInline, SkillInline]

    def has_add_permission(self, request):
        # Prevent adding a second profile; single-owner app
        if Profile.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")


admin.site.register([Certification, Project])

