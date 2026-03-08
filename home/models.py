from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]