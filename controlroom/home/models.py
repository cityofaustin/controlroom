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

class Blueprint(Page):
    # def __init__(self, *args, **kwargs):
    #     super(Blueprint, self).__init__(*args, **kwargs)
    #
    #     for stream_tuple in self.content.stream_data:
    #         if stream_tuple[0] == 'title':
    #             self.title = stream_tuple[1]
    #
    #     # we didn't find a title so fake it
    #     self.title = 'Untitled Blueprint'

    # title = models.CharField(
    #     max_length=255,
    #     editable=False
    # )

    # to reflect title of a current draft in the admin UI
    # TODO: figure out how this works
    # draft_title = models.CharField(
    #     max_length=255,
    #     editable=False
    # )

    content = StreamField(
      [
        ('caro', CarouselBlock(label="caro")),
        ('title', TextBlock(label="title"))
      ],
      blank=False
    )

    content_panels = [
      StreamFieldPanel('content')
    ]

    promote_panels = Page.content_panels + Page.promote_panels

    # def __str__(self):
    #
    #
    #   # # TODO: Figure out how to get this out of a streamfield
    #   #   # return self.text
    #   #   return "blarg"

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