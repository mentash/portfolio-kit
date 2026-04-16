from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


# Create blog index page model
class BlogIndexPage(Page):
    pass

# Create blog post model
class BlogPostPage(Page):
    pass

