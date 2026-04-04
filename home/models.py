from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string



class HomePage(Page):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True, default="")
    content = models.TextField(blank=True, default="")

    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
        FieldPanel("content"),
        FieldPanel("image"),
    
    ]