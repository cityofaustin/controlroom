from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core.blocks import StreamBlock, StructBlock, TextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.snippets.models import register_snippet

class CarouselBlock(StreamBlock):
    image = ImageChooserBlock()
    quotation = StructBlock([
        ('text', TextBlock()),
        ('author', CharBlock()),
    ])
    video = EmbedBlock()

    class Meta:
        icon='cogs'

@register_snippet
class Blueprint(models.Model):
    content = StreamField(
      [
        ('caro', CarouselBlock(label="caro")),
        ('text', TextBlock(label="text"))
      ],
      blank=False
    )

    panels = [
      StreamFieldPanel('content')
    ]

    def __str__(self):
      # TODO: Figure out how to get this out of a streamfield
        # return self.text
        return "blarg"

class HomePage(Page):
    content = StreamField(
      [
        ('caro', CarouselBlock(label="caro")),
        ('text', TextBlock(label="text"))
      ],
      blank=True
    )

    content_panels = Page.content_panels + [
      StreamFieldPanel('content')
    ]