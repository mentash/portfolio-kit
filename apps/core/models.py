from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        help_text='Enter a valid email address.',
        verbose_name='Email Address'
    )
    bio = models.TextField(
        blank=True,
        help_text='Write a short bio about yourself.',
        verbose_name='Biography'
    )

    def __str__(self):
        return self.name
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"
    
class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} from {self.issuing_organization}"
    
class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company}"

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)    
    proficiency = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Proficiency level from 1 to 10'
    )

    def __str__(self):
        return f"{self.name} (Proficiency: {self.proficiency}/10)"

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    
    experience = models.ManyToManyField(
        Experience, 
        blank=True, 
        through='ProjectExperience',
        related_name='projects'
    )

    def __str__(self):
        return self.name

# Intermediary model to link Projects and Experiences
class ProjectExperience(models.Model):
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE
    )
    
    experience = models.ForeignKey(
        Experience, 
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('project', 'experience')
