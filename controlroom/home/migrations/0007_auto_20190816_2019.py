# Generated by Django 2.2.4 on 2019-08-16 20:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190816_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprint',
            name='content',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.TextBlock(label='title')), ('page_type', wagtail.core.blocks.ChoiceBlock(choices=[('service_page', 'Service Page'), ('information_page', 'Information Page'), ('guide_page', 'Guide Page')], label='Page Type')), ('caro', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())], label='caro'))]),
        ),
    ]
