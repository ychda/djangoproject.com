# Generated by Django 6.0.dev20250403184043 on 2025-04-11 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_imageupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='social_media_card',
            field=models.ForeignKey(blank=True, help_text='For maximum compatibility, the image should be < 5 MB and at least 1200x627 px.', null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.imageupload'),
        ),
    ]
