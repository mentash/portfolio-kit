from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Education, Experience, Profile, Project, Skill


class HomeViewTests(TestCase):
    def test_home_shows_empty_state_when_no_profile_exists(self):
        """When no profile exists, home should show 404 empty state."""
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your portfolio has not been configured yet")

    def test_home_renders_single_profile_content(self):
        """Home renders the one profile and all its related data."""
        profile = Profile.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            bio="Backend engineer building useful things.",
        )

        Experience.objects.create(
            profile=profile,
            company="Acme",
            position="Software Engineer",
            start_date=date(2022, 1, 1),
            description="Built internal tools.",
        )

        Skill.objects.create(
            profile=profile,
            name="Django",
            proficiency=9,
        )

        Education.objects.create(
            profile=profile,
            institution="State University",
            degree="BSc",
            field_of_study="Computer Science",
            start_date=date(2018, 1, 1),
            end_date=date(2021, 1, 1),
        )

        Project.objects.create(
            profile=profile,
            name="Portfolio Kit",
            description="Personal portfolio project.",
        )

        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")
        self.assertContains(response, "Backend engineer building useful things.")
        self.assertContains(response, "Software Engineer")
        self.assertContains(response, "Django")
        self.assertContains(response, "Portfolio Kit")
        self.assertNotContains(response, "Your portfolio has not been configured yet")


class ProfileModelTests(TestCase):
    def test_profile_string_representation(self):
        profile = Profile.objects.create(name="Jane Doe", email="jane@example.com")
        self.assertEqual(str(profile), "Jane Doe")


class ExperienceOrderingTests(TestCase):
    def test_experience_orders_by_most_recent_first(self):
        """Experience should order by most recent start_date first."""
        profile = Profile.objects.create(name="Test", email="test@example.com")

        exp1 = Experience.objects.create(
            profile=profile,
            company="Old Co",
            position="Dev",
            start_date=date(2020, 1, 1),
        )
        exp2 = Experience.objects.create(
            profile=profile,
            company="New Co",
            position="Senior Dev",
            start_date=date(2022, 1, 1),
        )

        experiences = list(profile.experience.all())
        self.assertEqual(experiences[0], exp2)  # Most recent first
        self.assertEqual(experiences[1], exp1)


class SkillOrderingTests(TestCase):
    def test_skills_order_by_proficiency_descending(self):
        """Skills should order by proficiency (highest first)."""
        profile = Profile.objects.create(name="Test", email="test@example.com")

        skill1 = Skill.objects.create(profile=profile, name="JavaScript", proficiency=7)
        skill2 = Skill.objects.create(profile=profile, name="Python", proficiency=9)
        skill3 = Skill.objects.create(profile=profile, name="CSS", proficiency=6)

        skills = list(profile.skills.all())
        self.assertEqual(skills[0], skill2)  # Proficiency 9
        self.assertEqual(skills[1], skill1)  # Proficiency 7
        self.assertEqual(skills[2], skill3)  # Proficiency 6