from django.contrib import admin
from .models import Profile, Education, Certification, Experience, Skill, Project

# Register your models here.

# Admin classes to manage related models inline with Profile

# Admin class for Education to be displayed inline with Profile
class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    
# Admin class for Experience and Skill to be displayed inline with Profile
class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

# Admin class for Skill to be displayed inline with Profile
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

# Admin class for Profile to include Education, Experience, and Skill inlines
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [EducationInline, ExperienceInline, SkillInline]

# Registering Certification and Project models separately
admin.site.register([Certification, Project])